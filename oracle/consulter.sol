pragma solidity ^0.4.0;

import "mortal.sol";
import "oracle.sol";

contract Consulter is Mortal {

    event ConsulterOracleResponse(
        string _response
    );

    Oracle oracle;

    function Consulter(address _oracle) public {
        oracle = Oracle(_oracle);
    }

    function requestSomething() public {
        oracle.query("whatever", this.oracleResponse);
    }

    function oracleResponse(string _response) public {
        require(msg.sender == address(oracle));
        ConsulterOracleResponse(_response);
    }

}

