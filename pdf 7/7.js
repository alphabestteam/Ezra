

const bobs_friends = ['sandy', 'patrick', 'squidward', 'Mr. krabs', 'Gary'];

document.write(`bob has ${bobs_friends.length} friends - ${bobs_friends} <br>`);

bobs_friends.push('Mrs. puff');

document.write(`bob's updated list of friends (${bobs_friends.length} friends) - ${bobs_friends} <br>`);

bobs_friends[0] = 'moshe';

document.write(bobs_friends);

// the reason we can change the array is because we're only changing the value of the array
// and not the location. so for example "bobs_friends = ['ari','moshe','david']" would not be allowed.

