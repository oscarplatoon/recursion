exports.factorial = function(num) {
  if (num === 1) return num
  else {
    return factorial(num - 1) * num
  }
};

exports.palindrome = function(string) {
  if (string.length < 2) return true
  if (str[0] === str[strLen - 1]) {
    return isPalindrome( string.slice(1, string.length- 1) );
}
return false
};

exports.bottles = function(num) {
  let bottles = num
  phrase = console.log(`Take one down and pass it around, 1 bottle of beer on the wall.\n1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\nNo more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, ${bottles} bottles of beer on the wall.`)
  if (bottles < 2) return phrase
  console.log(`${bottles} bottles of beer on the wall, 99 bottles of beer.\nTake one down and pass it around, ${bottles} bottles of beer on the wall.`)
  return bottles(bottles - 1)
};

exports.romanNum = function(num) {

};
