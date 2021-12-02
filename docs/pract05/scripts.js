const navToggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.links');
const listItem = document.querySelectorAll('.list-item');
const arch_vis = document.querySelector('.arch_vis');
const prod_vis = document.querySelector('.prod_vis');
const mo_graph = document.querySelector('.mo_graph');
const photo = document.querySelector('.photo');
const design = document.querySelector('.design');
const web = document.querySelector('.web');
const art_dir = document.querySelector('.art_dir');

navToggle.addEventListener('click', () => {
    links.classList.toggle('show-links');
})

console.log(prod_vis)

listItem.forEach(function (btn) {
    btn.addEventListener('click', (e) => {
        // console.log(e.currentTarget)
        const show = e.currentTarget.classList;
        // console.log(show)
        if(show.contains('prod')) {
            prod_vis.classList.replace('select', 'show');
            arch_vis.classList.replace('show', 'select');
            mo_graph.classList.replace('show', 'select');
            photo.classList.replace('show', 'select');
            design.classList.replace('show', 'select');
            web.classList.replace('show', 'select')
            art_dir.classList.replace('show', 'select');
        }else if(show.contains('mo')) {
            mo_graph.classList.replace('select', 'show');
            prod_vis.classList.replace('show', 'select');
            photo.classList.replace('show', 'select');
            design.classList.replace('show', 'select');
            web.classList.replace('show', 'select');
            art_dir.classList.replace('show', 'select');
            arch_vis.classList.replace('show', 'select');
        }else if(show.contains('ph')) {
            photo.classList.replace('select','show');
            mo_graph.classList.replace('show', 'select');
            prod_vis.classList.replace('show', 'select');
            arch_vis.classList.replace('show', 'select');
            design.classList.replace('show', 'select');
            web.classList.replace('show', 'select');
            art_dir.classList.replace('show', 'select');
        }else if(show.contains('de')) {
            design.classList.replace('select', 'show');
            photo.classList.replace('show', 'select');
            mo_graph.classList.replace('show', 'select');
            prod_vis.classList.replace('show', 'select');
            web.classList.replace('show', 'select');
            art_dir.classList.replace('show', 'select');
            arch_vis.classList.replace('show', 'select');
        }else if(show.contains('wb')) {
            web.classList.replace('select', 'show');
            design.classList.replace('show', 'select');
            mo_graph.classList.replace('show', 'select');
            prod_vis.classList.replace('show', 'select');
            arch_vis.classList.replace('show', 'select');
            photo.classList.replace('show', 'select');
            art_dir.classList.replace('show', 'select');
        }else if(show.contains('art')) {
            art_dir.classList.replace('select', 'show');
            web.classList.replace('show', 'select');
            mo_graph.classList.replace('show', 'select');
            prod_vis.classList.replace('show', 'select');
            arch_vis.classList.replace('show', 'select');
            photo.classList.replace('show', 'select');
            design.classList.replace('show', 'select');
        }else{
            arch_vis.classList.replace('select', 'show');
            art_dir.classList.replace('show', 'select');
            mo_graph.classList.replace('show', 'select');
            prod_vis.classList.replace('show', 'select');
            photo.classList.replace('show', 'select');
            design.classList.replace('show', 'select');
            web.classList.replace('show', 'select');
        }
    })

    // prod_vis.classList.toggle('show');
})
