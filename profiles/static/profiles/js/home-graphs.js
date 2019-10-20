google.charts.load('current', { 'packages': ['corechart', 'geochart'], 'mapsApiKey': 'AIzaSyDfq6jzJpQxH4AXGUbpX-h0RzhvTUuOSkU' });
google.charts.setOnLoadCallback(init);

function drawPieChart(divId, nbProfiles, totProfiles, label, color1) {
    const data = new google.visualization.DataTable();
    data.addColumn('string', 'Position');
    data.addColumn('number', 'Entries in Repository');

    data.addRows([
        [label, nbProfiles],
        ['Rest', totProfiles - nbProfiles]
    ]);

    const options = {
        colors: ['#dedede', '#dedede'],
        fontName: 'Open Sans',
        fontSize: 14,
        chartArea: { left: '10%', top: 0, width: '80%', height: '100%' },
        width: 120,
        height: 120,
        legend: 'none',
        pieSliceText: 'none',
        pieHole: 0.6,
        enableInteractivity: false,
        slices: [{ color: color1, textStyle: { color: '#555555', fontName: 'Open Sans', fontSize: 18 } },
        { textStyle: { color: '#ffffff', fontName: 'Open Sans', fontSize: 1 } }]
    };

    const Piechart = new google.visualization.PieChart(document.getElementById(divId));

    Piechart.draw(data, options);
}

function drawMap(divId, jsonData) {
    const dataTable = jsonData.filter(country => country.profiles_count > 0)
        .map(country => [country.name, country.profiles_count]);
    dataTable.unshift(['Country', 'Profiles']);
    const data = google.visualization.arrayToDataTable(dataTable, false);

    const options = {
        colorAxis: { colors: ['#a0c1c1', '#10898B'] },
        legend: 'none',
        tooltip: { isHtml: false },
    };

    const chart = new google.visualization.GeoChart(document.getElementById(divId));
    chart.draw(data, options);
}

function percentString(decimal) {
    return (decimal * 100).toFixed(0) + '%';
}

function init() {
    $.ajax({
        url: '/api/countries/?format=json',
        dataType: "json",
        success: json => drawMap('regions_div', json)
    });

    $.ajax({
        url: '/api/positions/?format=json',
        dataType: "json",
        success: json => {
            let totProfiles = 0;
            const profiles = {
                'senior': 0,
                'postdoc': 0,
                'student': 0,
                'other': 0
            }
            json.forEach(pos => {
                totProfiles += pos.profiles_count;
                if (pos.position.match(/senior|lecturer|professor|director|principal/i)) {
                    profiles.senior += pos.profiles_count;
                }
                else if (pos.position.match(/post-doc/i)) {
                    profiles.postdoc += pos.profiles_count;
                }
                else if (pos.position.match(/phd\sstudent/i)) {
                    profiles.student += pos.profiles_count;
                }
                else {
                    profiles.other += pos.profiles_count;
                }
            });

            $('#student-percent').text(percentString(profiles.student / totProfiles));
            $('#postdoc-percent').text(percentString(profiles.postdoc / totProfiles));
            $('#senior-percent').text(percentString(profiles.senior / totProfiles));
            $('#other-percent').text(percentString(profiles.other / totProfiles));

            $('#student-count').text(profiles.student + ' profiles');
            $('#postdoc-count').text(profiles.postdoc + ' profiles');
            $('#senior-count').text(profiles.senior + ' profiles');
            $('#other-count').text(profiles.other + ' profiles');

            $('#entries-number').text(totProfiles);

            drawPieChart('chartPhD', profiles.student, totProfiles, 'PhD students', '#CC063E');
            drawPieChart('chartPostDoc', profiles.postdoc, totProfiles, 'Post-doc', '#E83535');
            drawPieChart('chartSenior', profiles.senior, totProfiles, 'Senior', '#FD9407');
            drawPieChart('chartOther', profiles.other, totProfiles, 'Other', '#999999');
        }
    });
}
