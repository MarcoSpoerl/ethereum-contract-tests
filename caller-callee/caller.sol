pragma solidity ^0.4.0;

import "mortal.sol";
import "callee.sol";

contract Caller is Mortal {

    Callee callee;

    function Caller(address _calleeAddress) public {
        callee = Callee(_calleeAddress);
    }

    function makeCall(uint8 number) constant returns (uint256 callResult) {
        callResult = callee.cube(number);
    }

}

