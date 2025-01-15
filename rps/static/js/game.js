const room_id = document
  .getElementById("game-info")
  .getAttribute("data-room_id");

const gameSocket = new WebSocket(
  "ws://" + window.location.host + `/ws/game/${room_id}`
);

const timer = document.getElementById("timer");

let seconds = 9;
let choice;
let time_flag=false

let timer_display=setInterval(()=>{
  if(seconds > 0 && time_flag){
    timer.innerHTML = `Timer : ${seconds}`;
  }
  else if(seconds == 0){
    timer.innerHTML = `Timer : ${seconds}`;
    if(choice == undefined){
      info={"choice" : "None"};
      gameSocket.send(JSON.stringify(info));
    }
  }
  else{
    clearInterval();
  }
  if (time_flag){
    seconds --;
  }
},1000);



document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("click", () => {
    choice = card.getAttribute("id");
    console.log(choice);
    let info={
      "choice" : choice,
    }
    gameSocket.send(JSON.stringify(info));
  });
});

gameSocket.onopen = function (event) {
  
};

gameSocket.onmessage = function (event) {
  let data=JSON.parse(event.data);

  if(data["start"]=="yes"){
    let game=document.getElementById("game");
    let gamegame=document.getElementById("gamegame");
    game.style.display = 'none';
    gamegame.style.display = 'block';
    time_flag=true;
  }
  else{
    let modal_input=document.getElementById("modal-input");
    if(data["winner"] == undefined){
      modal_input.innerHTML =  `Your Choice : ${data["choice"]}`;
      const myModal = new bootstrap.Modal(document.getElementById("myModal"));
      myModal.show();
  }
  else{
    modal_input.innerHTML= data["winner"];
    let restart_btn=document.getElementById("restart-btn");
    restart_btn.classList.toggle("d-none");
  }
}

};

gameSocket.onclose = function (event) {
  alert("Room Full");
  window.location = 'http://' +  window.location.host + '/';
};

gameSocket.onerror = function(event) {
  console.log(event)
}
