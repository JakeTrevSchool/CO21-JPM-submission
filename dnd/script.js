const races = ["Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc", "Human", "Tiefling"];
const classes = ['Barbarian','Bard','Cleric','Druid','Fighter','Monk','Paladin','Ranger','Rogue','Sorcerer','Warlock','Wizard','Artificer','Blood Hunter'];
const abilities = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma'];
const save = abilities.map((elm) => "save_" + elm);
const skills = ['athletics', 'deception', 'insight', "intimidation", "perception", "stealth"];
const skill_labels = skills.map(elm => elm.charAt(0).toUpperCase() + elm.slice(1))
const abil_labels = abilities.map(elm => elm.charAt(0).toUpperCase() + elm.slice(1));

function setIndividualAtt(className, max, label){
    const classes = document.getElementsByClassName(className);
    var values = [];
    var max_val = 0;
    Array.prototype.forEach.call(classes, (elm, ind) => {
        var value;
        if (ind == 3){
            value = max_val + Math.ceil(Math.random()*4);
            if (value > max) value = max;
        }else{
            value = Math.ceil(Math.random()*max);
            if (value > max_val) max_val = value;
        }
        elm.innerText = label + ": " + value;
    })
}

function setRandomChoices(choices, className, label){
    const classes = document.getElementsByClassName(className);
    Array.prototype.forEach.call(classes, (elm) => {
        elm.innerText = label + ": " + choices[Math.floor(Math.random()*choices.length)];
    });
}

function setRandomGroup(group, labels){
    group.map((att) => {
        var values = [];
        var max_val = 0;
        attClasses = document.getElementsByClassName(att);
        Array.prototype.forEach.call(attClasses, (elm, ind) => {
            var value;
            if (ind == 3){
                value = max_val + Math.ceil(Math.random()*4);
                if (value > 30) value = 30;
            }else{
                value = Math.ceil(Math.random()*30);
                if (value > max_val) max_val = value;
            }
            values.push(value);
            elm.innerText = labels[ind] + ": " + value;
        })
    });
}

function generate(){
     
    // set race
    setRandomChoices(races, 'race', "Race");

    // set class
    setRandomChoices(classes, 'class', "Class")

    // set level
    setIndividualAtt('level', 20, "Level");

    // Set abilities
    setRandomGroup(abilities, abil_labels);

    // set save abilities
    setRandomGroup(save, abil_labels);

    // set skills
    setRandomGroup(skills, skill_labels);

    // set armour
    setIndividualAtt('armour', 10, "Armour");

    // set initiative
    setIndividualAtt('initiative', 10, "Initiative");

    // set speed
    setIndividualAtt('speed', 40, "Speed");
    
}

generate();