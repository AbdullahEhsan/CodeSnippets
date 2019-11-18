let prices = [0,2,4,1,6,2,5,6]

func cutRod(pricelist: [Int], length: Int) -> Int{
  var F = Array(repeating: 0, count: length+1)
  for i in 0...length{
    var temp = 0
    for j in 0...i{
      temp = max(temp, pricelist[i-j] + F[j])
    }
    F[i] = temp
    print(F)
  }
  print(F)
  return F[length]
}

print(cutRod(pricelist: prices, length: 6))