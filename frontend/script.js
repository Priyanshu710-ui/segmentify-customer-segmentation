const fileInput =
    document.getElementById("fileInput");

const fileName =
    document.getElementById("fileName");

const analyzeBtn =
    document.getElementById("analyzeBtn");

const message =
    document.getElementById("message");

const segmentsContainer =
    document.getElementById(
        "segmentsContainer"
    );

const totalCustomers =
    document.getElementById(
        "totalCustomers"
    );

const totalSegments =
    document.getElementById(
        "totalSegments"
    );

const statusText =
    document.getElementById(
        "statusText"
    );


function scrollToUpload() {

    document
        .getElementById("uploadSection")
        .scrollIntoView({

            behavior: "smooth"

        });

}


fileInput.addEventListener(
    "change",
    function () {

        if (
            fileInput.files.length > 0
        ) {

            fileName.textContent =
                fileInput.files[0].name;

        }

    }
);


analyzeBtn.addEventListener(
    "click",
    async function () {

        if (
            fileInput.files.length === 0
        ) {

            message.textContent =
                "Please select a CSV file.";

            return;

        }


        analyzeBtn.disabled = true;

        analyzeBtn.textContent =
            "Analyzing...";

        message.textContent =
            "";

        statusText.textContent =
            "Analyzing";


        const formData =
            new FormData();

        formData.append(

            "file",

            fileInput.files[0]

        );


        try {

            const response =
                await fetch(

                    "/api/analyze",

                    {

                        method: "POST",

                        body: formData

                    }

                );


            const data =
                await response.json();


            if (!data.success) {

                throw new Error(
                    data.error
                );

            }


            totalCustomers.textContent =
                data.total_customers;

            totalSegments.textContent =
                data.clusters;

            statusText.textContent =
                "Complete";


            displaySegments(
                data.segments
            );


            message.textContent =
                "✓ Analysis completed successfully!";


            document
                .getElementById("segments")
                .scrollIntoView({

                    behavior: "smooth"

                });


        } catch (error) {

            message.textContent =
                "Error: " +
                error.message;

            statusText.textContent =
                "Error";

        }


        analyzeBtn.disabled = false;

        analyzeBtn.textContent =
            "✦ Analyze Customers";

    }
);



function displaySegments(
    segments
) {

    segmentsContainer.innerHTML =
        "";


    segments.forEach(

        function (segment) {

            const card =
                document.createElement(
                    "div"
                );

            card.className =
                "segment-card";


            let averagesHTML =
                "";


            for (
                const [key, value]
                of Object.entries(
                    segment.averages
                )
            ) {

                averagesHTML += `

                    <div class="average-row">

                        <span>
                            ${key}
                        </span>

                        <strong>
                            ${value}
                        </strong>

                    </div>

                `;

            }


            card.innerHTML = `

                <div class="segment-number">

                    ${String(
                        segment.segment
                    ).padStart(
                        2,
                        "0"
                    )}

                </div>


                <h3>
                    ${segment.name}
                </h3>


                <p class="customer-count">

                    ${segment.customers}
                    customers in this segment.

                </p>


                <div class="averages">

                    ${averagesHTML}

                </div>

            `;


            segmentsContainer.appendChild(
                card
            );

        }

    );

}