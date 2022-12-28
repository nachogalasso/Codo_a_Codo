// CALLING THE HTML ELEMENTS
const bgColor = document.querySelector('.container');
const label = document.querySelector('.hide');
const property = document.getElementById('prop'); // Display the background property
// const colorInput = [...document.getElementsByTagName("input")];
const colorInput = [...document.querySelectorAll('.color')];
const degInput = [...document.querySelectorAll('.deg')];
const gradients = [...document.querySelectorAll('.grad')];
const ort = document.getElementById('ort')
const container = document.querySelector(".container");
let hex = [...document.querySelectorAll(".hex-text")];
const copyBtn = document.querySelector('.fa-copy');

const copyToClipboard = str => (
	navigator.clipboard?.writeText?.(str)
	?? Promise.reject('The Clipboard is not working')
)



let colorDOM = ["#000000", "#ffffff"]
let degDOM = [0, 0]
let gradient = "";
let direction = "";
property.value = `background: ${gradient}-gradient(${direction}deg, ${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;

document.addEventListener('DOMContentLoaded', getProperty)


function getColors() {
	// const colorInput = [...document.getElementsByTagName("input")];
	colorInput.forEach((pick) => {
		pick.addEventListener("change", (e) => {
			let picked = e.target;

			if (picked.classList.contains("c1")) {
				colorDOM[0] = e.target.value;
				hex[0].textContent = `Hex: ${colorDOM[0]}`;
			}
			if (picked.classList.contains("c2")) {
				colorDOM[1] = e.target.value;
				hex[1].textContent = `Hex: ${colorDOM[1]}`;
			}
			
			getProperty()

			// if (picked.classList.contains("deg1")) {
         //    degDOM[0] = e.target.value;
			// }
			// if (picked.classList.contains("deg2")) {
			// 	degDOM[1] = e.target.value;
			// }
			


         //  if (picked.id === "linear") {
			// 		label.classList.add("show");
			// 		gradient = picked.value;
			// 	} else if (picked.id === "ort") {
			// 		direction = picked.value;
			// 		property.value = `background: ${gradient}-gradient(${direction}deg, ${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`
			// 	}

			// 	if (picked.id === "radial" || picked.id === "conic") {
			// 		label.classList.remove("show");
			// 		gradient = picked.value;
			// 		property.value = `background: ${gradient}-gradient(${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;
			// 	}

			// 	getProperty()
            // container.style = property.value
			
		});
	});
}

function getDeg() {
	degInput.forEach(pick => {
		pick.addEventListener("change", (e) => {
			if(e.target.classList.contains('d1')) {
				degDOM[0] = e.target.value
			}else{
				degDOM[1] = e.target.value
			}

		getProperty();

		})
	})
}

function getProperty() {
	getColors()
	getDeg()
	gradients.forEach((pick) => {
		pick.addEventListener("change", (e) => {
			let picked = e.target.id;
			
			if (picked === "linear") {
				label.classList.add("show");
				gradient = e.target.value;
				ort.addEventListener('change', (e) => {
					direction = e.target.value
					property.value = `background: ${gradient}-gradient(${direction}deg, ${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;
					container.style = property.value;
				})
			}

			if (picked === "radial" || picked === "conic") {
				label.classList.remove("show");
				gradient = e.target.value;
				property.value = `background: ${gradient}-gradient(${colorDOM[0]} ${degDOM[0]}%, ${colorDOM[1]} ${degDOM[1]}%);`;
				container.style = property.value;
			}
		});
	});
}

copyBtn.addEventListener('click', async () => {
	try {
		await copyToClipboard(property.value)
	}catch(err){
		console.error(err)
	}
})