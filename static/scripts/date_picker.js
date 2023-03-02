if (window.location.pathname === "/") {
    const selectElement = document.querySelector('select')

    // Set minimum date to current date
    const datePicker = document.getElementById('date-picker')
    const today = new Date().toISOString().slice(0, -14)
    // datePicker.min = today
    datePicker.value = today
    const maxDate = new Date(new Date(today).setMonth(new Date().getMonth() + 6)).toISOString().slice(0, -14)
    datePicker.max = maxDate

    // Populating time slots

    const appointmentTimes = [] // Receive available appointment times from database

    populateTimeSlots(appointmentTimes)

    function populateTimeSlots(appTimesArray) {
        for (i in appTimesArray) {
            const option = document.createElement("option")
            option.value = appTimesArray[i]
            option.innerText = appTimesArray[i]
            selectElement.append(option)
        }
    }

    // Find out if there is available appointments at selected date and get error messages, if any. Select next available date
    isDateAvailable(datePicker)

    const month30 = ['04', '06', '09', '11']
    const month31 = ['01', '03', '05', '07', '08', '10', '12']

    function isLeapYear(year) {
        //  Credits to Adrian Holovaty for this function
        return (
            ((year % 4) === 0) && 
            ((year % 100) !== 0 ) || 
            ((year % 400) === 0)
        )
    }

    function dateChosen(target, inputField) {
        let year = target.getFullYear()
        
        let month = target.getMonth() + 1
        if (month < 10) month = `0${month}`
        
        let date = target.getDate()
        if (date < 10) date = `0${date}`

        let choiceIndex = target.getDay()
        let errorMessage = ''

        // Saturday
        if (choiceIndex === 6) {
            
            if (date == '28' && [...month30, ...month31].includes(month)){ 
                date = '30'                                // date 28 = 30 in month w/ 30, 31 days
            } else if (
                date == '29' && month30.includes(month) || // date 29 = 01 in month w/ 30 days
                date == '30' && month31.includes(month)) { // date 30 = 01 in month w/ 31 days
                date = '01'
                month = `0${parseInt(month) + 1}`
            } else if (
                date == '30' && month30.includes(month) || // date 30 = 02 in month w/ 30 days
                date == '31' && month31.includes(month) || // date 31 = 02 in month w/ 31 days
                ![...month30, ...month31].includes(month) && date === '29' && isLeapYear(year)  // 29/02 leap year
            ) {
                date = '02'
                month = `0${parseInt(month) + 1}`
            } else if (![...month30, ...month31].includes(month) && date === '27' && isLeapYear(year)) {    // 27/02 leap year
                date = '29'
            } else if (
                ![...month30, ...month31].includes(month) && date === '27' ||   // 27/02 not leap year
                ![...month30, ...month31].includes(month) && date === '28' && isLeapYear(year)) { // 28/02 leap year
                date = '01'
                month = `0${parseInt(month) + 1}`
            // } else if () { // TBC
                // date = `01`
            } else {
                let dateNum = parseInt(date)
                date = dateNum <= 7 ? `0${dateNum + 2}` : `${dateNum + 2}`
            }
            

            inputField.value = `${year}-${month}-${date}`

            errorMessage = `Unfortunately, Saturday isn't available for appointments.`
        }

        // Sunday
        if (choiceIndex === 0) {
            if (date == '28' && [...month30, ...month31].includes(month)){ 
                date = '29'                                // date 28 = 29 in month w/ 30, 31 days
            } else if (date == '29' && [...month30, ...month31].includes(month) // date 29 = 30 in month w/ 30, 31 days
            ) {
                date = '30'
            }else if (
                date == '30' && month31.includes(month)) { // date 30 = 01 in month w/ 31 days
                date = '31'
            } else if (
                date == '30' && month30.includes(month) || // date 30 = 01 in month w/ 30 days
                date == '31' && month31.includes(month)    // date 31 = 01 in month w/ 31 days
            ) {
                date = '01'
                month = `0${parseInt(month) + 1}`
            } else if (![...month30, ...month31].includes(month) && date === '27') {
                date = '28'
            } else if (![...month30, ...month31].includes(month) && date === '28') {
                date = '01'
                month = `0${parseInt(month) + 1}`
            } else {
                let dateNum = parseInt(date)
                date = dateNum <= 7 ? `0${dateNum + 2}` : `${dateNum + 2}`
            }
        
            inputField.value = `${year}-${month}-${date}`
            
            errorMessage = `Unfortunately, Sunday isn't available for appointments.`
        }

        return errorMessage
    }


    function isDateAvailable(inputField) {
        inputField.addEventListener('input', (e) => {
            const choice = new Date(e.target.value)
            dateChosen(choice, inputField)
        })
    }

    // Find out if there is available appointments at selected time

    function isTimeSlotAvailable(app) {
        for (let i in app) {
            if (appointmentTimes.includes(app[i])) {
                const available = []
                available.push(app[i])
                return available
            }
        }
    }
}
