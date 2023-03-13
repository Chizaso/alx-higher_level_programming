#!/usr/bin/node
function callMeMoby (x, theFunction) {
  Array.from({ length: x }, () => theFunction());
}
module.exports = { callMeMoby };
