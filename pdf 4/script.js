/*
Your job for today is to finish the starSign function.

Find the astrological sign, given the birth details as a Date object.
Start and end dates for zodiac signs very on different resources, 
so we will use this table to get consistent testable results:

Aquarius ----- 21 January - 19 February
Pisces ----- 20 February - 20 March
Aries ----- 21 March - 20 April
Taurus ----- 21 April - 21 May
Gemini ----- 22 May - 21 June
Cancer ----- 22 June - 22 July
Leo ----- 23 July - 23 August
Virgo ----- 24 August - 23 September
Libra ----- 24 September - 23 October
Scorpio ------ 24 October - 22 November
Sagittarius ----- 23 November - 21 December
Capricon ------ 22 December - 20 January
*/

function starSign(date) {
    const months = ["January", "February", "March",
        "April", "May", "June", "July", "August",
        "September", "October", "November", "December"];

    try {
        const d = new Date(date);
        switch (months[d.getMonth()]) {

            case "January":
                if (d.getDate() <= 20) {
                    return "Capricon";
                }
                else {
                    return "Aquarius";
                }

            case "February":
                if (d.getDate() <= 19) {
                    return "Aquarius";
                }
                else {
                    return "Pisces";
                }

            case "March":
                if (d.getDate() <= 20) {
                    return "Pisces";
                }
                else {
                    return "Aries";
                }

            case "April":
                if (d.getDate() <= 20) {
                    return "Aries";
                }
                else {
                    return "Taurus";
                }

            case "May":
                if (d.getDate() <= 21) {
                    return "Taurus";
                }
                else {
                    return "Gemini";
                }

            case "June":
                if (d.getDate() <= 21) {
                    return "Gemini";
                }
                else {
                    return "Cancer";
                }

            case "July":
                if (d.getDate() <= 22) {
                    return "Cancer";
                }
                else {
                    return "Leo";
                }

            case "August":
                if (d.getDate() <= 23) {
                    return "Leo";
                }
                else {
                    return "Virgo";
                }

            case "September":
                if (d.getDate() <= 23) {
                    return "Virgo";
                }
                else {
                    return "Libra";
                }

            case "October":
                if (d.getDate() <= 23) {
                    return "Libra";
                }
                else {
                    return "Scorpio";
                }

            case "November":
                if (d.getDate() <= 22) {
                    return "Scorpio";
                }
                else {
                    return "Sagittarius";
                }

            case "December":
                if (d.getDate() <= 21) {
                    return "Sagittarius";
                }
                else {
                    return "Capricon";
                }

        }
    } catch {
        return "not a date";
    }

}

let date_of_birth = prompt(`what's you're date of birth?`, `year-month-day`);
document.write(`<h1>${starSign(date_of_birth)}</h1>`);
