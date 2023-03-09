import {reactive} from "vue"

export const colorStore = reactive({
    
    colorsPicked: {
        color: "",
        deg: 0,
    },

    colorPair: []
})

// export function addColors() {
    
//    colorStore.colorPair = []
//    const cp = colorStore.colorsPicked.color;
//    const dg = colorStore.colorsPicked.deg;
//    for (let c in colorStore.colorsPicked) {
//     colorStore.colorPair.push({
//         id: crypto.randomUUID(),
//         color: cp,
//         deg: dg,
//     })
//         colorStore.colorPair.id++
//    }
 
//     console.log(colorStore)
//     console.log(colorStore.colorPair)


// }
// export function setColor() {
//     if (this.picked === "linear") {
//         return `background: ${this.picked}-gradient(${this.orientation}deg, ${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
//     } else {
//         return `background: ${this.picked}-gradient(${this.fcolor} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
//     }
// }
export function setColor() {
   
    return `background: ${this.picked}-gradient(45deg, ${this.color} ${this.fstop}%, ${this.scolor} ${this.sstop}%)`;
    
}