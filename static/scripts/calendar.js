function isLeapYear(year) {
    // Adrian Holovaty
    return (
        ((year % 4) === 0) && 
        ((year % 100) !== 0 ) || 
        ((year % 400) === 0)
    )
}

function getDaysInMonth(month, year) {
    // Adrian Holovaty

    let days;
    if (month === 1 || 
        month === 3 || 
        month === 5 || 
        month === 7 || 
        month === 8 || 
        month === 10 || 
        month === 12) {
        days = 31
    }
    else if (
        month === 4 || 
        month === 6 || 
        month === 9 || 
        month === 11) {
        days = 30;
    }
    else if (
        month === 2 && 
        isLeapYear(year)) {
        days = 29;
    }
    else {
        days = 28;
    }
    return days;
}

let monthsInYear = {
    1 : "January", 
    2 : "February", 
    3 : "March", 
    4 : "April", 
    5 : "May", 
    6 : "June", 
    7 : "July", 
    8 : "August", 
    9 : "September", 
    10 : "October", 
    11 : "November", 
    12 : "December"
}

let daysAvailable = {
    1: 'Monday',
    2: 'Tuesday', 
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday'
}

function drawCalendar() {
    let todayDate = new Date()
    let month = parseInt(todayDate.getMonth())
    let date = parseInt(todayDate.getDate())
    
    for (const key in monthsInYear) {
        if (monthsInYear.hasOwnProperty(key)) {
        }
      }
}