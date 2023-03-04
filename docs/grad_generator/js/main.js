const form = document.querySelector('.color__form');

const app = Vue.createApp({
	data: () => ({
		title: "Gradient Generator",
		fcolor: "#ffffff",
		scolor: "#000000",
		bcolor: "#cecece",
		fstop: 0,
		sstop: 0,
		ncolor: 0,
		nstop: 0,
		orientation: 0,
		picked: [],
	}),

	methods: {
		createNewColor() {
            const newColor = document.createElement('section');
            newColor.classList.add('colors');
            newColor.innerHTML = `
                <!-- 3rd COLOR -->
                  <label for="lcolor" class="label_color">C3:
                      <input type="color" name="color" id="lcolor" class="icolor" v-model="bcolor">
                  </label>
                  <label for="deg" class="deg_label">%:
                      <input type="number" name="deg" id="deg" min="0" max="0" v-model="bstop">
                  </label>
                  <p class="text">HEX 3: {{bcolor}}</p>
            `;
			
            form.append(newColor)
            console.log(form)
		},
	},

	computed: {
		// function that allows to see the our background property
		setColor() {
			if (this.picked === "linear") {
				return `background: ${this.picked}-gradient(${this.orientation}deg, ${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
			} else {
				return `background: ${this.picked}-gradient(${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
			}
		},
	},
}); 

