console.log("test")
d3.json("http://localhost:5000/education").then(function(response){
    console.log(response)
    policy_holder_array = response.map(function(element){return element.policy_holder})
    console.log(policy_holder_array)

    console.log(response)
    policy_holder_count = response.map(function(element){return element.n})
    console.log(policy_holder_count)

    var ctx = document.getElementById('myChart').getContext('2d');
    var pie_chart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: policy_holder_array,
            datasets: [{
                label: '# of Votes',
                data: policy_holder_count,
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)',
                    'rgba(255, 206, 86, 0.2)',
                    'rgba(75, 192, 192, 0.2)',
                    'rgba(153, 102, 255, 0.2)',
                    'rgba(255, 159, 64, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)',
                    'rgba(255, 206, 86, 1)',
                    'rgba(75, 192, 192, 1)',
                    'rgba(153, 102, 255, 1)',
                    'rgba(255, 159, 64, 1)'
                ],
                borderWidth: 1
            }]
        },
        options:{
            tooltips: {
                callbacks: {
                    title: function([tooltipItem], data){
                        console.log(data)
                        var education = data.labels[tooltipItem.index]
                        return education;
                    },
                    label: function(tooltipItem, data) {
                        var value = data.datasets[0].data[tooltipItem.index]
                        var title = `${value}`
                        return title;
                    }
                }  
            }
        }

    })


}).catch(function(error){if (error)throw error})

