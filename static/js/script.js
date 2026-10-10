// ===============================
// Attendance Doughnut Chart
// ===============================
const attendance = document.getElementById("attendanceChart");

if (attendance) {
    new Chart(attendance, {
        type: "doughnut",
        data: {
            labels: ["Present", "Absent"],
            datasets: [{
                data: [89, 11],
                backgroundColor: [
                    "#22c55e",
                    "#ef4444"
                ],
                borderWidth: 2
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: "bottom"
                }
            }
        }
    });
}


// ===============================
// Marks Bar Chart
// ===============================
const marks = document.getElementById("marksChart");

if (marks) {
    new Chart(marks, {
        type: "bar",
        data: {
            labels: ["AI", "ML", "CN", "Cyber"],
            datasets: [{
                label: "Marks",
                data: [90, 84, 88, 92],
                backgroundColor: [
                    "#2563eb",
                    "#16a34a",
                    "#f59e0b",
                    "#ef4444"
                ],
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            scales: {
                y: {
                    beginAtZero: true,
                    max: 100
                }
            },
            plugins: {
                legend: {
                    display: false
                }
            }
        }
    });
}