const TEST = 'palindrome';

// Using Recursion
reverseString = (str) => {
  if(str === '') return '';
  return reverseString(str.substr(1)) + str.charAt(0);
}

// Using for loop
reverse = (str) => {
  let reverse = '';
  for(let i=(str.length-1);i>=0;i--){
    reverse += str[i];
  }
  return reverse;
}



console.log(reverse(TEST) === 'emordnilap');
console.log(reverseString(TEST) === 'emordnilap');
