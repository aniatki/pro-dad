if (window.location.pathname === "/") {
    const selectElement = document.querySelector('select')

    // Set minimum date to current date
    const datePicker = document.getElementById('date-picker')
    const today = new Date().toISOString().slice(0, -14)
    datePicker.setAttribute('min', today)
    datePicker.value = today

    // Populating time slots

    const appointmentTimes = [
        "09:00",
        "10:30",
        "12:00",
        "14:30",
        "16:00",
        "17:30",
    ]
    
    const appointmentsAvailable = [
        "09:00",
        "10:30",
        "12:00",
    ]
    populateTimeSlots(appointmentTimes)

    function populateTimeSlots(appTimesArray) {
        for (i in appTimesArray) {
            const option = document.createElement("option")
            option.value = appTimesArray[i]
            const newList = appointmentsAvailable.filter(app => app != option.value) 
            console.log(newList)
            option.innerText = appTimesArray[i]
            selectElement.append(option)
        }
    }

    // Return selected timeslot

    // selectElement.addEventListener("change", (e) => e.target.value)

    // Find out what date is picked

    function checkPickedDate() {}

    // Find out if there is available appointments at selected date and get error messages, if any. Select next available date
    isDateAvailable(datePicker)

    function isDateAvailable(inputField) {
        inputField.addEventListener('input', (e) => {
            const choice = new Date(e.target.value)
            
            let year = choice.getFullYear()
            
            let month = choice.getMonth() + 1
            if (month < 10) month = "0" + month
            
            let date = choice.getDate()
            if (date < 10) date = "0" + date
            
            let choiceIndex = choice.getDay()

            if (choiceIndex === 6) {
                if (date === 28 && month === 1 || 
                    date === 29 && month === 1) date = -1
                if (date === 30) date = -1
                if (date === 31) date = 0
                
                inputField.value = `${year}-${month}-${date + 2}`
                
                return `Unfortunately, Saturday isn't available for appointments.`
            }
            
            if (choiceIndex === 0) {
                if (date === 28 && month === 1 || 
                    date === 29 && month === 1) date = 0
                if (date === 30) date = 0
                if (date === 31) date = 1
            
                inputField.value = `${year}-${month}-${date + 1}`
            
                return `Unfortunately, Sunday isn't available for appointments`
            }
            
            // Add more _if_ statements to check for availability
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