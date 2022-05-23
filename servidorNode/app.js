var thrift = require("thrift");
var CalculatorService = require("./gen-nodejs/CalculatorService");

var server = thrift.createServer(CalculatorService, {
  multiplicar: function(n1,n2){
    return n1 * n2
  },

  dividir: function(n1,n2){
    return n1 / n2
  },
  
  sumar: function(n1,n2){
    return n1 + n2
  },

  restar: function(n1,n2){
    return n1 - n2
  }

});

server.listen(9090);
console.log('escuchando en 9090')