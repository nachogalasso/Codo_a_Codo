app.component('color', {
    template:`
    <section class="colors">
        <label for="lcolor" class="label_color">C 1:
            <input type="color" name="color" id="lcolor" class="icolor" v-model="fcolor">
        </label>
        <label for="deg" class="deg_label">%:
            <input type="number" name="deg" id="deg" min="0" max="0" v-model="fstop">
        </label>
        <p class="text">HEX 1: {{fcolor}}</p>
    </section>
        <label for="lcolor" class="label_color">C 2:
            <input type="color" name="color" id="lcolor" class="icolor" v-model="scolor">
        </label>
        <label for="deg2" class="deg_label">%:
            <input type="number" name="deg2" id="deg2" min="0" max="0" v-model="sstop">
        </label>
        <p class="text">HEX 2: {{scolor}}</p>
    `,

    data: () => ({
        fcolor: '#EA0606',
        scolor: '#000000',
        fstop: 0,
        sstop: 0
    })
})