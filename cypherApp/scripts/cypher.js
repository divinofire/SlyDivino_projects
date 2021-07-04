// import and use this in your js projects :::: import {cypher} from './cypher.js'; 
// for interactive cypher in command line, use cypherConsole.js instead


function cypher(text, shift){ // shift is a number between 0 and 26 and text is the text you wish to decipher.
	function correctIndex(index_, shift){  // make sure index lies between 0 and 25 when a shift is applied

			let index = index_ + shift;


			if (index > 25) index = index%26; 
			else if (index < 0 && index > -26 ) index = 26 + index;
			else if (index < -25) {index = 26 + index%26; index = (index == 26)?0:index}
			return index;
}


	let alphabet = 'abcdefghijklmnopqrstuvwxyz';
	let alphabet_caps = alphabet.toUpperCase(); // was not used in this simple cypher program, you can extend this program to make use of it.

	let new_text = '';
	let new_letter = '';
	let new_index ;

	for (letter in text) {
		let old_index = alphabet.indexOf(text[letter]);

		if (old_index>=0){

			new_index = correctIndex(old_index, shift); // get the new index of our letter
			new_letter = alphabet[new_index];
			new_text += new_letter;  // append new letter to our new cyphered text

		}
		else { // if letter doesn't exist in alphabet, leave the letter unchanged.

			new_text += text[letter];
		}		

	}	

	return new_text;
}

// ---- code ends here -----

module.exports = cypher;

// 	function log(variable, value){ // function to be used for debugging purposes only

// 	console.log(`${variable} : ${value}`);

// }