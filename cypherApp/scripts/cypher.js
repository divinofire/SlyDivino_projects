// import and use this in your js projects :::: import {cypher} from './cypher.js'; 
// for interactive cypher in command line, use cypherConsole.js instead


function cypher(text, shift){ // shift is a number between 0 and 26 and text is the text you wish to decipher.
	let alphabet = 'ZaY0:bXc1WdVe2.UfT3gShRiQ;jPkOlNmM_nLoKpJ ,q4IrH5sGt6FuE7vDwC8xB9yAz'; // create a character array as a lookup dictionary
	function correctIndex(lookup_array, index_, shift){  //function to make sure index lies between 0 and alphabet length when a shift is applied

			let index = index_ + shift; // get shifted index
			if (index > (lookup_array.length - 1)) index = index % (lookup_array.length); 
			else if (index < 0 && index > -(lookup_array.length)) index = (lookup_array.length) + index;
			else if (index < -(lookup_array.length -1)) {
				index = (lookup_array.length) + index%(lookup_array.length);
				index = (index == (lookup_array.length))? 0:index;
			}
			return index;
	}

	

	let new_text = '';
	let new_letter = '';
	let new_index ;

	for (letter in text) {
		let old_index = alphabet.indexOf(text[letter]); //get letter from text and find its index in alphabet

		if (old_index>=0){ 

			new_index = correctIndex(alphabet, old_index, shift); // get the new index of our letter after applying a shift
			new_letter = alphabet[new_index]; // get new letter from alphabet based on new index
			new_text += new_letter;  // append new letter to our new cyphered text

		}
		else { // if letter doesn't exist in alphabet, leave the letter unchanged in its same position

			new_text += text[letter]; 
		}		

	}	

	return new_text;
}

// ---- code ends here -----

module.exports = cypher;  // export cypher to use as module elsewhere via `import cypher from cypher or var cypher = require("cypher")`

// 	function log(variable, value){ // function to be used for debugging purposes only

// 	console.log(`${variable} : ${value}`);

// }