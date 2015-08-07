$('p').fadeOut();

function describePerson(person) {
  var stringDescription = person.name +
  ", favorite color: " +
   person.color;

   if (person.artist != undefined) {
      stringDescription = stringDescription + ", favorite artist: " + person.artist;
   }
  return stringDescription;
}


console.log(describePerson("Renee"));

var cssiFolks = [];

cssiFolks.push( {"name" : "Riccardo", "color" : "orange", "artist" : "kandinsky"} );
cssiFolks.push( {"name" : "Roger", "color" : "blue"} );
cssiFolks.push( {"name" : "Elizabeth", "color" : "purple"} );
cssiFolks.push( {"name" : "Bex", "color" : "green", "artist" : "piccasso"} );



for( var index = 0 ; //this is a variable within the array
   index < cssiFolks.length ; index++ ) {
  console.log(describePerson(cssiFolks[index]))
}
