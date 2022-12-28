// SPDX-License-Identifier: MIT
pragma solidity >=0.6.0 <0.9.0;

// Importar AggregatorV3Interface
import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";

contract FundMe {
    AggregatorV3Interface public priceFeed;

    constructor(address _priceFeed) public {
        owner = msg.sender;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    mapping(address => uint256) public addresstoAmountFunded; // quantidade doada.
    address public owner;
    address[] public Funders;
    modifier isADM() {
        require(msg.sender == owner);
        _;
    }

    function fund() public payable {
        uint256 minUSD = 50 * 10**18;
        require(getConversionRate(msg.value) >= minUSD, "Not enough ETH!!!");
        addresstoAmountFunded[msg.sender] += msg.value; // msg -> quem chama a função no momento.
        Funders.push(msg.sender);
    }

    // Cuidado pra pegar o address da rede certa!
    function getVersion() public view returns (uint256) {
        return priceFeed.version();
    }

    function getPrice() public view returns (uint256) {
        (, int256 value, , , ) = priceFeed.latestRoundData();
        return uint256(value * 10**10);
    }

    function getConversionRate(uint256 ethAmount)
        public
        view
        returns (uint256)
    {
        uint256 ethusd = getPrice();
        uint256 usdAmount = (ethusd * ethAmount) / 10**18; // Smart Contracts sempre trabalham a nivel Wei
        return usdAmount;
    }

    function withdraw() public payable isADM {
        payable(msg.sender).transfer(address(this).balance);
        for (uint256 index = 0; index < Funders.length; index++) {
            address funder = Funders[index];
            addresstoAmountFunded[funder] = 0;
        }

        Funders = new address[](0);
    }

    function getEntranceFee() public view returns (uint256) {
        // getprice brings in with 10**18, minUSD scaled to 10**18 as well,and then precision allows accurate calculus.
        uint256 minUSD = 50 * 10**18;
        uint256 price = getPrice();
        uint256 precision = 1 * 10**18;
        return (precision * minUSD) / price + 1; //Applying suggested correction on GitHub repo issues section
    }
}
