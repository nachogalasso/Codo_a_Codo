// HTML elements
//stats
const gameStats = [...document.querySelectorAll(".stat")]; // create an array instead of a nodelist
//btns
const gameBtns = document.querySelectorAll(".action-btn");
// player game display
const xpText = document.querySelector(".xpText");
const healthText = document.querySelector(".healthText");
const goldText = document.querySelector(".goldText");
// monster game display
const monsterStats = document.querySelector(".monsterStats");
const monsterName = document.querySelector(".monsterName");
const monsterLife = document.querySelector(".monsterHealth");
const text = document.querySelector(".text p");

// Game control variables
let playerXP = 0;
let playerHealth = 100;
let gold = 50;
let currentWeapon = 0;
let fighting;
let monsterHealth;
let inventory = ["stick"];
const weapons = [
	{
		name: "stick",
		power: 5,
	},
	{
		name: "dagger",
		power: 30,
	},
	{
		name: "claw hammer",
		power: 50,
	},
	{
		name: "sword",
		power: 100,
	},
];

const monsters = [
	{
		name: "slime",
		level: 2,
		health: 15,
	},
	{
		name: "fanged beast",
		level: 8,
		health: 60,
	},
	{
		name: "dragon",
		level: 20,
		health: 300,
	},
];

const locations = [
	{
		name: "Town Square",
		"button text": ["Go to store", "Go to cave", "Fight dragon"],
		"button functions": [goToStore, goCave, fightDragon],
		text: 'You are in Town Square. You see a sign that says "store."',
	},
	{
		name: "store",
		"button text": [
			"Buy 10 health (10 gold)",
			"Buy Weapon (30 gold)",
			"Go to Town square",
		],
		"button functions": [buyHealth, buyWeapon, townDefault],
		text: "You enter the store",
	},
	{
		name: "Cave",
		"button text": ["fight slime", "fight fanged beast", "Go to Twon Square"],
		"button functions": [fightSlime, fightBeast, townDefault],
		text: "You have enter the cave. You see some monsters",
	},
	{
		name: "fight",
		"button text": ["attack", "dodge", "run"],
		"button functions": [attack, dodge, townDefault],
		text: "You are fighting a monster",
	},
	{
		name: "kill monster",
		"button text": [
			"go to town square",
			"go to town square",
			"go to town square",
		],
		"button functions": [townDefault, townDefault, easterEgg],
		text: "The monster screams, as it dies. You gain xp points and gold",
	},
	{
		name: "lose",
		"button text": ["replay?", "replay?", "replay?"],
		"button functions": [restart, restart, restart],
		text: "You die" + String.fromCodePoint(0x1f480),
	},
	{
		name: "win",
		"button text": ["replay?", "replay?", "replay?"],
		"button functions": [restart, restart, restart],
		text:
			"You defeat the dragon. YOU WIN THE GAME!!" +
			String.fromCodePoint(0x1f4aa),
	},
	{
		name: "easter egg",
		"button text": ["2", "8", "go to town square?"],
		"button functions": [pickTwo, pickEight, townDefault],
		text: "You find a secret game. Pick a number above. Ten numbers will be randomly chosen between 0 and 10. If the number you choose matches one of the random numbers, you WIN!"
	},
];

function update(location) {
	monsterStats.style.display = "none";
	gameBtns[0].textContent = location["button text"][0];
	gameBtns[1].textContent = location["button text"][1];
	gameBtns[2].textContent = location["button text"][2];
	gameBtns[0].onclick = location["button functions"][0];
	gameBtns[1].onclick = location["button functions"][1];
	gameBtns[2].onclick = location["button functions"][2];
	text.textContent = location.text;
}

function townDefault() {
	update(locations[0]);
}

// Game functionality
gameBtns[0].onclick = goToStore;
gameBtns[1].onclick = goCave;
gameBtns[2].onclick = fightDragon;

function goToStore() {
	update(locations[1]);
}

function goCave() {
	update(locations[2]);
}

function buyWeapon() {
	if (currentWeapon < weapons.length - 1) {
		if (gold >= 30) {
			gold -= 30;
			currentWeapon++;
			goldText.textContent = gold;
			let newWeapon = weapons[currentWeapon].name; // we put the new weapon in a variable we took it from the weapons array
			text.textContent = `You now have a ${newWeapon}.`;
			inventory.push(newWeapon);
			text.textContent = `In your invertory you have ${inventory}`;
		} else {
			text.textContent = "You do not have enough gold to buy a weapon.";
		}
	} else {
		text.textContent = "You already have the most powerful weapon!";
		gameBtns[2].textContent = "Sell weapon for 15 gold";
		gameBtns[2].onclick = sellWeapon;
	}
}

function buyHealth() {
	if (gold >= 10) {
		// compound assignment

		gold -= 10;
		goldText.textContent = gold;
		playerHealth += 10;
		healthText.textContent = playerHealth;
	} else {
		text.textContent = "You do not have enough gold to buy health";
	}
}

function sellWeapon() {
	// first to sell a weapon, we need to check if the inventory is > 1
	if (inventory.length > 1) {
		gold += 15;
		goldText.textContent = gold;
		let currentWeapon = inventory.shift();
		text.textContent = `You sold your ${currentWeapon}.`;
		text.textContent += `In your inventory you have left ${inventory}.`;
	} else {
		text.textContent =
			"You need weapons to fight, you cannot sell your only weapon";
	}
}
function fightSlime() {
	fighting = 0;
	goFight();
}

function fightBeast() {
	fighting = 1;
	goFight();
}

function fightDragon() {
	fighting = 2;
	goFight();
}

function goFight() {
	update(locations[3]);
	// here we tell the user what monster he is fighting
	monsterHealth = monsters[fighting].health;
	monsterStats.style.display = "block";
	monsterName.textContent = monsters[fighting].name;
	monsterLife.textContent = monsterHealth;
}

function attack() {
	// display text when monster attacks
	text.textContent = `The ${monsters[fighting].name} attacks. Watch out!!.`;
	// remember using the '+=' will add the text at the end of the first one
	text.textContent += ` You attacked with your ${weapons[currentWeapon].name}.`;
	// so if the monster attacks, we need to reduce the player health
	if(isMonsterHit()) {
		playerHealth -= getMonsterAttackValue(monsters[fighting].level);
	}else{
		text.textContent = 'You miss!!'
	}
	// at the end of monster attack we are gonna add a randon number for XP
	monsterHealth -=
		weapons[currentWeapon].power + Math.floor(Math.random() * playerXP) + 1;
	healthText.textContent = playerHealth;
	monsterLife.textContent = monsterHealth;
	if (playerHealth <= 0) {
		youLose();
	} else if (monsterHealth <= 0) {
		// fighting logic, we can use the ternary statement fighting === 2 ? youWin() : defeatMonster()
		if (fighting === 2) {
			youWin();
		} else {
			defeatMonster();
		}
	}
	// condition if the attacker´s weapon breaks
	if(Math.random() <= .1 && inventory.length !== 1) {
		text.textContent = "Your " + inventory.pop() + " breaks.";
		currentWeapon--;
	}
}

function getMonsterAttackValue(level) {
	let hit = (level * 5) - (Math.floor(Math.random() * playerXP));
	//  if I don´t put the return, I won´t have the value in playerHealth
	return hit
}

function isMonsterHit() {
	// we use Math.random( ) to create a random punch miss
	return Math.random() > .2 || playerHealth < 20;
}

function dodge() {
	text.textContent = `You dodge the attack from the ${monsters[fighting].name}.`;
}

function defeatMonster() {
	// we give the player gold for defeating the monster
	gold = Math.floor(monsters[fighting].level * 6.7);
	playerXP += monsters[fighting].level;
	goldText.textContent = gold;
	xpText.textContent = playerXP;
	text.textContent = `You defeat the ${monsters[fighting].name}.`;
	update(locations[4]);
}

function youLose() {
	update(locations[5]);
}

function youWin() {
	update(locations[6]);
}

function restart() {
	//  we set all the variables to default
	let playerXP = 0;
	let playerHealth = 100;
	let gold = 50;
	let currentWeapon = 0;
	let monsterHealth;
	let inventory = ["stick"];
	goldText.textContent = gold;
	healthText.textContent = playerHealth;
	xpText.textContent = playerXP;
	townDefault();
}

function easterEgg() {
	update(locations[7]);
}

function pickTwo() {
	pick(2)
}

function pickEight() {
	pick(8)
}

function pick(guess) {
	let numbers = []
	while(numbers.length < 10) {
		numbers.push(Math.floor(Math.random() * 11))
	}
	// \n at the end indicates to add a new line to the string
	text.textContent = 'You picked ' + guess + '. Here are the random numbers:\n';

	for (let i = 0; i < 10; i++) {
		text.textContent += numbers[i] + "\n";
	}

	if(numbers.indexOf(guess) !== -1) {
		text.textContent =
         "Right! You win 20 gold " + String.fromCodePoint(0x1f4b0);
		gold += 20;
		goldText.textContent = gold;
	}else{
		text.textContent = "Wrong! You lose 10 health";
		playerHealth -= 10;
		healthText.textContent = playerHealth;
		if(playerHealth <= 0) {
			youLose();
		}
	}
}