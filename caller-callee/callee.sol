pragma solidity ^0.4.0;

import "mortal.sol";

contract Callee is Mortal {

    function cube(uint8 number) constant returns (uint256 cubed) {
        cubed = number * number * number;
    }

}

