// Sort an array, 2
//
// Sort a given array, but not by alphabetically order, but by how long each
// name is, shortest name first.

var people = [
  'Dom',
  'Lyn',
  'Kirk',
  'Autumn',
  'Trista',
  'Jesslyn',
  'Kevin',
  'John',
  'Eli',
  'Juan',
  'Robert',
  'Keyur',
  'Jason',
  'Che',
  'Ben'
];

var res = people.sort((a, b) => a.length - b.length || a.localeCompare(b));
console.log(res);
