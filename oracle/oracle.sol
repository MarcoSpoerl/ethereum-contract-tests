pragma solidity ^0.4.0;

import "mortal.sol";

contract Oracle is Mortal {

    struct Request {
        function(string memory) external callback;
    }

    event OracleRequest(
        uint _requestId,
        string _someParameter
    );

    uint nextRequestId = 0;
    mapping (uint => Request) requests;

    function query(string _something, function(string memory) external _callback) public {
        requests[nextRequestId] = Request(_callback);
        OracleRequest(nextRequestId, _something);
        ++nextRequestId;
    }

    function reply(uint _requestId, string _response) public {
        requests[_requestId].callback(_response);
    }
  
}

