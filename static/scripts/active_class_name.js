const ulElem = document.querySelector('.ul-nav-links')
const li = ulElem.querySelectorAll('li') // Select all elements which the class name can be applied to
const homeLink = ulElem.children[0].firstChild
const myDashboardLink = ulElem.children[2].firstChild

li.forEach(tag => tag.addEventListener('click', onClickClassToggle)) // Loop through them and add click events

window.location.pathname == '/' ? homeLink.classList.add('active') : homeLink.classList.remove('active')
window.location.pathname == '/user_dashboard/' ? myDashboardLink.classList.add('active') : myDashboardLink.classList.remove('active')

function onClickClassToggle(e) {
    let target = e.target
    if (target.classList.value != 'active') target.classList.add('active') 
    // check if clicked element doesn't have the class name already, if so add it
    document.addEventListener('click', (ev) => { 
        // add another event listener to the document itself, 
        // if the currently clicked item doesn't match the previously clicked item, 
        // the class name will be removed from the previous item
        if (ev.target != target) target.classList.remove('active') 
    })
    document.querySelector('#menu-toggle').checked = false
}