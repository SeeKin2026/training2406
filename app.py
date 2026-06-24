import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Grammar Space Invaders",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 Grammar Space Invaders")

html_code = """

<!DOCTYPE html>

<html>

<head>

<style>

body{
margin:0;
overflow:hidden;
background:black;
font-family:Arial;
}

#container{
position:relative;
width:100%;
height:700px;
background:
radial-gradient(circle,#091540,#000814);
overflow:hidden;
}

#scoreboard{
position:absolute;
top:10px;
left:20px;
color:white;
font-size:24px;
font-weight:bold;
z-index:100;
}

#question{
position:absolute;
top:60px;
left:50%;
transform:translateX(-50%);
font-size:34px;
color:#FFD700;
font-weight:bold;
z-index:100;
}

.alien{
position:absolute;
font-size:70px;
cursor:pointer;
transition:0.2s;
}

.label{
font-size:28px;
background:#111;
border:3px solid lime;
padding:5px 15px;
border-radius:10px;
color:white;
}

#ship{
position:absolute;
bottom:30px;
left:50%;
transform:translateX(-50%);
font-size:90px;
}

.laser{
position:absolute;
width:6px;
height:40px;
background:red;
box-shadow:0 0 20px yellow;
}

.explosion{
position:absolute;
font-size:100px;
animation:boom 0.7s forwards;
}

@keyframes boom{

0%{
transform:scale(0.5);
opacity:1;
}

100%{
transform:scale(2);
opacity:0;
}

}

#feedback{

position:absolute;

bottom:140px;

width:100%;

text-align:center;

font-size:30px;

font-weight:bold;

color:white;

}

#explanation{

position:absolute;

bottom:90px;

width:100%;

text-align:center;

font-size:24px;

color:#00ffcc;

}

</style>

</head>

<body>

<div id="container">

<div id="scoreboard">

⭐ Score: <span id="score">0</span>

&nbsp;&nbsp;&nbsp;

❤️ Lives: <span id="lives">3</span>

</div>

<div id="question"></div>

<div id="feedback"></div>

<div id="explanation"></div>

<div id="ship">🚀</div>

</div>

<script>

const questions=[

{
sentence:"The dogs ____ in the park.",
correct:"run",
wrong:"runs",
explanation:"Many dogs = plural, so we use run."
},

{
sentence:"The cat ____ on the sofa.",
correct:"sits",
wrong:"sit",
explanation:"One cat = singular, so we use sits."
},

{
sentence:"Dad ____ coffee.",
correct:"drinks",
wrong:"drink",
explanation:"One dad = singular, so we use drinks."
},

{
sentence:"The children ____ to school.",
correct:"walk",
wrong:"walks",
explanation:"Children means many, so use walk."
},

{
sentence:"My sister ____ very fast.",
correct:"runs",
wrong:"run",
explanation:"One sister = singular, so use runs."
}

];

let score=0;

let lives=3;

const container=document.getElementById("container");

function nextQuestion(){

if(lives<=0){

container.innerHTML=`
<h1 style='color:red;
text-align:center;
padding-top:200px;'>

👾 GAME OVER

<br><br>

⭐ Score ${score}

</h1>
`;

return;
}

document.getElementById("feedback").innerHTML="";

document.getElementById("explanation").innerHTML="";

document.querySelectorAll(".alienbox").forEach(e=>e.remove());

const q=questions[Math.floor(Math.random()*questions.length)];

document.getElementById("question").innerHTML=q.sentence;

let answers=[q.correct,q.wrong];

answers.sort(()=>Math.random()-0.5);

answers.forEach((answer,index)=>{

let box=document.createElement("div");

box.className="alienbox";

box.style.position="absolute";

box.style.left=(25+index*40)+"%";

box.style.top="180px";

box.style.textAlign="center";

box.style.cursor="pointer";

box.innerHTML=`

<div class='alien'>👾</div>

<div class='label'>${answer}</div>

`;

container.appendChild(box);

box.onclick=function(){

shoot(box,answer,q);

};

});

}

function shoot(target,answer,q){

let laser=document.createElement("div");

laser.className="laser";

laser.style.left="50%";

laser.style.bottom="120px";

container.appendChild(laser);

let endY=420;

let position=120;

let animation=setInterval(()=>{

position+=15;

laser.style.bottom=position+"px";

if(position>=endY){

clearInterval(animation);

laser.remove();

explode(target,answer,q);

}

},20);

}

function explode(target,answer,q){

const rect=target.getBoundingClientRect();

let explosion=document.createElement("div");

explosion.className="explosion";

explosion.innerHTML="💥";

explosion.style.left=target.offsetLeft+"px";

explosion.style.top=target.offsetTop+"px";

container.appendChild(explosion);

target.remove();

setTimeout(()=>{

explosion.remove();

},700);

if(answer===q.correct){

score+=10;

document.getElementById("feedback").innerHTML="🎉 Great Shot!";

}

else{

lives-=1;

document.getElementById("feedback").innerHTML="😄 Nice Try!";

}

document.getElementById("explanation").innerHTML=q.explanation;

document.getElementById("score").innerHTML=score;

document.getElementById("lives").innerHTML=lives;

setTimeout(()=>{

nextQuestion();

},2500);

}

nextQuestion();

</script>

</body>

</html>

"""

components.html(
    html_code,
    height=750
)
