let poop = document.querySelector('.Stinkers');
let parsedStinker = parseFloat(poop.innerHTML);

let clickyCost = document.querySelector('.clickyCost');
let parsedClickyCost = parseFloat(clickyCost.innerHTML);

let clickyLevel = document.querySelector('.clickyLevel');
let clickyIncrease = document.querySelector('.clickyIncrease');
let parsedClickyIncrease = parseFloat(clickyIncrease.innerHTML);

let pickaxeCost = document.querySelector('.pickaxeCost');
let parsedPickaxeCost = parseFloat(pickaxeCost.innerHTML);

let pickaxeLevel = document.querySelector('.pickaxeLevel');
let pickaxeIncrease = document.querySelector('.pickaxeIncrease');
let parsedPickaxeIncrease = parseFloat(pickaxeIncrease.innerHTML);

let minerCost = document.querySelector('.minerCost');
let parsedMinerCost = parseFloat(minerCost.innerHTML);

let minerLevel = document.querySelector('.minerLevel');
let minerIncrease = document.querySelector('.minerIncrease');
let parsedMinerIncrease = parseFloat(minerIncrease.innerHTML);

let factoryCost = document.querySelector('.factoryCost');
let parsedFactoryCost = parseFloat(factoryCost.innerHTML);

let factoryLevel = document.querySelector('.factoryLevel');
let factoryIncrease = document.querySelector('.factoryIncrease');
let parsedFactoryIncrease = parseFloat(factoryIncrease.innerHTML);

let poopImageContainer = document.querySelector(".poop-image-container")

let spcText = document.getElementById("spcText");
let spsText = document.getElementById("spsText");

let spc = 1;

let sps = 0;

const upgrades = [ // this is for the save/load functions
    {
        name: "clicky",
        cost: document.querySelector(".clickerCost"),
        parsedCost: parseFloat(document.querySelector(".clickyCost").innerHTML),
        increase: document.querySelector(".clickyIncrease"),
        parsedIncrease: parseFloat(document.querySelector(".clickyIncrease").innerHTML),
        level: document.querySelector(".clickyLevel"),
        poopMultiplier: 1.03,
        costMultiplier: 1.18,
    },
    {
        name: "pickaxe",
        cost: document.querySelector(".pickaxeCost"),
        parsedCost: parseFloat(document.querySelector(".pickaxeCost").innerHTML),
        increase: document.querySelector(".pickaxeIncrease"),
        parsedIncrease: parseFloat(document.querySelector(".pickaxeIncrease").innerHTML),
        level: document.querySelector(".pickaxeLevel"),
        poopMultiplier: 1.03,
        costMultiplier: 1.18,
    },
    {
        name: "miner",
        cost: document.querySelector(".minerCost"),
        parsedCost: parseFloat(document.querySelector(".minerCost").innerHTML),
        increase: document.querySelector(".minerIncrease"),
        parsedIncrease: parseFloat(document.querySelector(".minerIncrease").innerHTML),
        level: document.querySelector(".minerLevel"),
        poopMultiplier: 1.21,
        costMultiplier: 1.32,
    },
    {
        name: "factory",
        cost: document.querySelector(".factoryCost"),
        parsedCost: parseFloat(document.querySelector(".factoryCost").innerHTML),
        increase: document.querySelector(".factoryIncrease"),
        parsedIncrease: parseFloat(document.querySelector(".factoryIncrease").innerHTML),
        level: document.querySelector(".factoryLevel"),
        poopMultiplier: 1.32,
        costMultiplier: 1.50,
    }
]

function incrementStinkers(event) {
    poop.innerHTML = Math.round(parsedStinker += spc);

    const x = event.offsetX
    const y = event.offsetY

    const div = document.createElement('div');
    div.innerHTML = `+${Math.round(spc)}`
    div.style.cssText = `color: white; position: absolute; top: ${y}px; left: ${x}px; font-size: 20px; pointer-events: none;`
    poopImageContainer.appendChild(div);

    div.classList.add('fade-up')

    timeout(div)
};

const timeout = (div) => {
    setTimeout(() => {
        div.remove();
    }, 800);
}

function buyClicky() {
    if (parsedStinker >= parsedClickyCost) {
        poop.innerHTML = Math.round(parsedStinker -= parsedClickyCost);

        clickyLevel.innerHTML ++;

        parsedClickyIncrease = parseFloat((parsedClickyIncrease * 1.03).toFixed(2));
        clickyIncrease.innerHTML = parsedClickyIncrease;
        spc += parsedClickyIncrease;

        parsedClickyCost *= 1.18;
        clickyCost.innerHTML = Math.round(parsedClickyCost)
    };
};

function buyPickaxe() {
    if (parsedStinker >= parsedPickaxeCost) {
        poop.innerHTML = Math.round(parsedStinker -= parsedPickaxeCost);

        pickaxeLevel.innerHTML ++; // Corrected line

        parsedPickaxeIncrease = parseFloat((parsedPickaxeIncrease * 1.03).toFixed(2));
        pickaxeIncrease.innerHTML = parsedPickaxeIncrease;
        sps += parsedPickaxeIncrease;

        parsedPickaxeCost *= 1.18;
        pickaxeCost.innerHTML = Math.round(parsedPickaxeCost);
    }
}

function buyMiner() {
    if (parsedStinker >= parsedMinerCost) {
        poop.innerHTML = Math.round(parsedStinker -= parsedMinerCost);

        minerLevel.innerHTML ++; // Corrected line

        parsedMinerIncrease = parseFloat((parsedMinerIncrease * 1.21).toFixed(2));
        minerIncrease.innerHTML = parsedMinerIncrease;
        sps += parsedMinerIncrease;

        parsedMinerCost *= 1.32;
        minerCost.innerHTML = Math.round(parsedMinerCost);
    }
}

function buyFactory() {
    if (parsedStinker >= parsedFactoryCost) {
        poop.innerHTML = Math.round(parsedStinker -= parsedFactoryCost);

        factoryLevel.innerHTML ++; // Corrected line

        parsedFactoryIncrease = parseFloat((parsedFactoryIncrease * 1.32).toFixed(2));
        factoryIncrease.innerHTML = parsedFactoryIncrease;
        sps += parsedFactoryIncrease;

        parsedFactoryCost *= 1.50;
        factoryCost.innerHTML = Math.round(parsedFactoryCost);
    }
}

function save() {
    localStorage.clear();

    upgrades.map((upgrade) => {

        const obj = JSON.stringify({
            parsedLevel: parseFloat(upgrade.level.innerHTML),
            parsedCost: upgrade.parsedCost,
            parsedIncrease: upgrade.parsedIncrease,
        })

        localStorage.setItem(upgrade.name, obj);

    })

    localStorage.setItem('spc', JSON.stringify(spc));
    localStorage.setItem('sps', JSON.stringify(sps));
    localStorage.setItem('Stinkers', JSON.stringify(parsedStinker));
}

function load() {
    upgrades.map((upgrade) => {
        const savedValues = JSON.parse(localStorage.getItem(upgrade.name)) || {};

        if (savedValues.parsedCost !== undefined) {
            upgrade.parsedCost = savedValues.parsedCost;
            upgrade.parsedIncrease = savedValues.parsedIncrease;
            upgrade.level.innerHTML = savedValues.parsedLevel;
            upgrade.cost.innerHTML = Math.round(upgrade.parsedCost);
            upgrade.increase.innerHTML = upgrade.parsedIncrease;
        }

        poop.innerHTML = Math.round(parsedStinker);
    });
}

setInterval(() => {
    parsedStinker += sps / 10;
    poop.innerHTML = Math.round(parsedStinker);
    spcText.innerHTML = Math.round(spc);
    spsText.innerHTML = Math.round(sps);
}, 100)
