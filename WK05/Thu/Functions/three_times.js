// 3 times
//
// Given this function:
//
// function call3Times(fun) {
//   fun();
//   fun();
//   fun();
// }
// Use the call3Times function to print "Hello, world!" 3 times.
//

function call3Times(fun) {
  fun();
  fun();
  fun();
}

function hello() {
  console.log('Hello, world!');
};

call3Times(hello);
