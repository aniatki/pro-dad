if (window.location.pathname === "/") {
    const selectElement = document.querySelector('select')

    // Set minimum date to current date
    const datePicker = document.getElementById('date-picker')
    const today = new Date().toISOString().slice(0, -14)
    datePicker.min = today
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

    function dateChosen(target, inputField) {
        let year = target.getFullYear()
            
            let month = target.getMonth() + 1
            if (month < 10) month = "0" + month
            
            let date = target.getDate()
            if (date < 10) date = "0" + date
            
            let choiceIndex = target.getDay()

            let errorMessage = ''

            if (choiceIndex === 6) {
                if (date === 28 && month === 1 || 
                    date === 29 && month === 1) date = -1
                if (date === 30) date = -1
                if (date === 31) date = 0
                
                inputField.value = `${year}-${month}-${date + 2}`

                errorMessage = `Unfortunately, Saturday isn't available for appointments.`
            }

            if (choiceIndex === 0) {
                if (date === 28 && month === 1 || 
                    date === 29 && month === 1) date = 0
                if (date === 30) date = 0
                if (date === 31) date = 1
            
                inputField.value = `${year}-${month}-${date + 1}`
                
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
