// CALLING THE HTML ELEMENTS
const bgColor = document.querySelector('.container');
const label = document.querySelector('.hide');
const property = document.getElementById('prop'); // Display the background property
const colorInput = [...document.getElementsByTagName("input")];
const container = document.querySelector(".container");

console.log(container)
let colorDOM = ["#000000", "#ffffff"]
let degDOM = [0, 0]
let gradient = "";
let direction = "";


document.addEventListener('DOMContentLoaded', getColors)

// async function getColors() {
//    try {
//       // const colorInput = [...document.getElementsByTagName("input")];
//       colorInput.forEach(pick => {
//          pick.addEventListener('change', (e) => {
//             let picked = e.target;
//             if (picked.classList.contains("c1")) {
// 					colorDOM[0] = picked.value;
// 				}
// 				if (picked.classList.contains("c2")) {
// 					colorDOM[1] = picked.value;
// 				}
// 				if (picked.classList.contains("deg1")) {
// 					return degDOM[0] = picked.value;
// 				}
// 				if (picked.classList.contains("deg2")) {
// 					return degDOM[1] = picked.value;
// 				}
//             // getValues(picked)
//             displayHex(colorDOM);
//             linearData(picked)
            
            
//             // property.value = `background: ${gradient}-gradient(circle, ${colorDOM[0].color} ${colorDOM[0].deg}%, ${colorDOM[1].color} ${colorDOM[1].deg}%);`;
//             const container = document.querySelector(".container").style = property.value

//          })
//       })
      
//    }catch (err) {
//       console.log(err)
//    }
// }

function getColors() {
	// const colorInput = [...document.getElementsByTagName("input")];
	colorInput.forEach((pick) => {
		pick.addEventListener("change", (e) => {
			let picked = e.target;
			if (picked.classList.contains("c1")) {
				colorDOM[0] = picked.value;
			}
			if (picked.classList.contains("c2")) {
				colorDOM[1] = picked.value;
			}
			if (picked.classList.contains("deg1")) {
            degDOM[0] = e.target.value;
            console.log(degDOM)
			}
			if (picked.classList.contains("deg2")) {
				degDOM[1] = e.target.value;
			}
			// getValues(picked)
			// displayHex(colorDOM);
			// linearData(picked, colorDOM, degDOM);
         let hex = [...document.querySelectorAll(".hex-text")];
			hex[0].textContent = `hex: ${colorDOM[0]}`;
			hex[1].textContent = `hex: ${colorDOM[1]}`;


          if (picked.id === "linear") {
					label.classList.add("show");
					gradient = picked.value;
				} else if (picked.id === "ort") {
					direction = picked.value;
					property.value = `background: ${gradient}-gradient(${direction}deg, ${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`
				}

				if (picked.id === "radial" || picked.id === "conic") {
					label.classList.remove("show");
					gradient = picked.value;
					property.value = `background: ${gradient}-gradient(${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`
				}
            console.log(property.value)
            container.style = property.value
			
		});
	});
}

// function displayHex(colorDOM) {
//    let hex = [...document.querySelectorAll(".hex-text")];
//    hex[0].textContent = `hex: ${colorDOM[0]}`
//    hex[1].textContent = `hex: ${colorDOM[1]}`
// }

// function linearData(picked, colorDOM, degDOM) {
   
//    if (picked.id === 'linear') {
//       label.classList.add('show') 
//       gradient = picked.value
//    }else if(picked.id === 'ort') {
//       direction = picked.value;
//       return property.value = `background: ${gradient}-gradient(${direction}deg, ${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;
//    }
   
//    if (picked.id === 'radial' || picked.id === 'conic') {
//       label.classList.remove('show')
//       gradient = picked.value
//       return property.value = `background: ${gradient}-gradient(${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;
//    }
// }
