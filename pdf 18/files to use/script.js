const speciesPoints = {
    'pink spotted': 4,
    'blue stinger': 3,
    'green itches': 2,
    'common': 1
};

const jellyfishDays = [
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
        { color: 'white' },
        { color: 'white' },
    ],
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
        { color: 'green' },
        { color: 'green' },
    ],
    [
        { color: 'pink' },
        { color: 'pink' },
        { color: 'pink' },
        { color: 'pink' },
        { color: 'blue' },
        { color: 'green' },
    ]
];

// SpongeBob's net callback function
function catchJellyfish(jellyfish, identifyJellyfishAndAddPoints) {
    console.log(`SpongeBob caught a ${jellyfish} jellyfish!`);
    return identifyJellyfishAndAddPoints(jellyfish, scoreKeeper);

}

// Patrick's net callback function
function identifyJellyfishAndAddPoints(jellyfish, scoreKeeper) {

    const species = identifySpecies(jellyfish)
    console.log(`Patrick identified a ${species} jellyfish!`);
    const score = scoreKeeper(species);
    console.log(`Score: ${score}`);
    return score;
}

// Score keeping callback function
function createScoreKeeper() {
    let counter = 0;
    // did a closure so that the counter will be private.
    function addPoints(species) {

        counter += speciesPoints[species];
        return counter;
    }
    return addPoints;
}

// Helper functions
function identifySpecies(jellyfish) {
    switch (jellyfish) {
        case 'pink':
            return 'pink spotted';
        case 'blue':
            return 'blue stinger';
        case 'green':
            return 'green itches';
        default:
            return 'common';
    }
}

//The Adventure Starts Here! 
console.log(`Let's go jellyfishing!`);
const scoreKeeper = createScoreKeeper();
let finalScore = 0;

// iterating foreach day iterate over it's fish.
jellyfishDays.forEach(day => {
    day.forEach(fish => {
        finalScore = catchJellyfish(fish['color'], identifyJellyfishAndAddPoints);
    });
    console.log(`Final score: ${finalScore}`);
    console.log(`********************`);
});



