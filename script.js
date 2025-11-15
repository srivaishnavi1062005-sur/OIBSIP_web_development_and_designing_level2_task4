document.addEventListener('DOMContentLoaded', function () {
    // Attach event listeners after the DOM has fully loaded
    document.querySelectorAll('.remove-btn').forEach(button => {
        attachRemoveButton(button);
    });

    document.getElementById('leaveHomeBtn').addEventListener('click', function () {
        const switches = document.querySelectorAll('#applianceContainer input[type="checkbox"]');
        let anyOn = false;
        switches.forEach(switchEl => {
            if (switchEl.checked) {
                anyOn = true;
            }
        });

        if (anyOn) {
            document.getElementById('alert').classList.remove('hidden');
        } else {
            alert("All appliances are off. You can safely leave your home!");
            document.getElementById('alert').classList.add('hidden');
        }
    });

    document.getElementById('addApplianceBtn').addEventListener('click', function () {
        const applianceName = prompt("Enter the name of the new appliance:");
        if (applianceName) {
            const container = document.getElementById('applianceContainer');
            const newAppliance = document.createElement('div');
            newAppliance.classList.add('appliance', 'd-flex', 'flex-column', 'justify-content-center');
            newAppliance.innerHTML = `
                <label class="texts">${applianceName}:</label>
                <input type="checkbox" data-name="${applianceName}">
                <button class="remove-btn">&times;</button>
            `;
            container.appendChild(newAppliance);

            // Attach remove function to the new remove button
            const newRemoveBtn = newAppliance.querySelector('.remove-btn');
            attachRemoveButton(newRemoveBtn);
        }
    });
});
