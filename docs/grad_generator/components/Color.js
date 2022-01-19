app.component('color', {
    template:`
    <section class="colors">
        <label for="ncolor" class="label_color">Cn:
            <input type="color" name="color" id="ncolor" class="icolor" v-model="ncolor">
        </label>
        <label for="deg" class="deg_label">%:
            <input type="number" name="deg" id="deg" min="0" max="0" v-model="nstop">
        </label>
        <p class="text">HEX 1: {{ncolor}}</p>
    </section>
    `,

    props: {
        color: String,
        deg: Number,
    }
})