const selectElement = document.querySelector('select')

const dayIndex = new Date().getDay()

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

function populateTimeSlots(appTimesArray) {
    for (i in appTimesArray) {
        const option = document.createElement("option")
        option.value = appTimesArray[i]
        option.innerText = appTimesArray[i]
        selectElement.append(option)
        // option.setAttribute('disabled', 'true')
    }
}
populateTimeSlots(appointmentTimes)

// Return selected time
selectElement.addEventListener("change", (e) => e.target.value)

// Find out what date is picked

function checkPickedDate() {}

// Find out if there is available appointments at selected date

function isDateAvailable() {}

// If not, select the next available date

function getNextDate() {}

// Find out what time is picked

function checkPickedTimeSlot() {}

// Find out if there is available appointments at selected time

function isTimeSlotAvailable() {}

// If not, select the next available time

function getNextTimeSlot() {}

