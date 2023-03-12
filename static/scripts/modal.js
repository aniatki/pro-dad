// Modal stuff
const modal = document.querySelector(".modal")
const openBtn = document.querySelector('.leave-review')
const closeBtn = document.querySelector('.close-modal')

openBtn.addEventListener("click", () => {
    modal.showModal()
})
