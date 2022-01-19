const app = Vue.createApp({
    data: () => ({
        title: 'Gradient Generator',
        fcolor: '#ffffff',
        scolor: '#000000',
        fstop: 0,
        sstop: 0,
        ncolor: 0,
        nstop: 0,
        orientation: 0,
        picked: [],

        
    }),
    
    computed: {
        // function that allows to see the our background property
        setColor() {
            if(this.picked === 'linear') {
                
                return `background: ${this.picked}-gradient(${this.orientation}deg, ${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;

            }else{

                return `background: ${this.picked}-gradient(${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;

            }
        }
    },

    
}) 

