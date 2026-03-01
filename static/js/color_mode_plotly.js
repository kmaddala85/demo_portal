document.addEventListener("DOMContentLoaded", () => {

    // Select all dropdown buttons using their unique ids (e.g., themeDropdown1, themeDropdown2)
    const themeDropdowns = document.querySelectorAll('.dropdown-menu');

    // Function to update Plotly background
    function updatePlotBackground(theme) {
        const isDarkMode = (theme === 'dark') ? true : false;
        
        // Define layout changes for Plotly
        const plotLayout = {
                            annotationdefaults:  {arrowcolor: isDarkMode ? '#f2f5fa': '#2a3f5f'
                                                },      
                            paper_bgcolor: isDarkMode ? 'rgb(17,17,17)' :  'white',
                            plot_bgcolor: isDarkMode ? 'rgb(17,17,17)' : '#E5ECF6',
                            polar:  {angularaxis: {gridcolor: isDarkMode ? '#506784' : 'white', 
                                                linecolor: isDarkMode ? '#506784': 'white'},
                                    bgcolor: isDarkMode ? 'rgb(17,17,17)' : '#E5ECF6',
                                    radialaxis: {gridcolor: isDarkMode ? '#506784': 'white', 
                                                linecolor: isDarkMode ? '#506784': 'white'}
                                    },
                            scene:  {xaxis: {backgroundcolor: isDarkMode ? 'rgb(17,17,17)' : '#E5ECF6',
                                            gridcolor: isDarkMode ?  '#283442': 'white',
                                            linecolor: isDarkMode ? '#506784': 'white',
                                            zerolinecolor: isDarkMode ? '#283442': 'white'},
                                    yaxis: {backgroundcolor: isDarkMode ? 'rgb(17,17,17)' : '#E5ECF6',
                                            gridcolor: isDarkMode ? '#283442': 'white',
                                            linecolor: isDarkMode ? '#506784': 'white',
                                            zerolinecolor: isDarkMode ? '#283442': 'white'},
                                    zaxis: {backgroundcolor:isDarkMode ?  'rgb(17,17,17)' : '#E5ECF6',
                                            gridcolor: isDarkMode ? '#283442': 'white',
                                            linecolor: isDarkMode ? '#506784': 'white',
                                            zerolinecolor: isDarkMode ? '#283442': 'white'}
                                    },
                            xaxis: {gridcolor: isDarkMode ? '#283442': 'white',
                                    linecolor: isDarkMode ? '#506784': 'white',
                                    zerolinecolor: isDarkMode ? '#283442': 'white',
                                    title: {'standoff': 15}
                                }, 
                            yaxis: {gridcolor: isDarkMode ? '#283442': 'white',
                                    linecolor: isDarkMode ? '#506784': 'white',
                                    zerolinecolor: isDarkMode ? '#283442': 'white',
                                    title: {'standoff': 15},
                                },
                            ternary: {aaxis: {gridcolor: isDarkMode ? '#506784': 'white', 
                                            linecolor: isDarkMode ? '#506784': 'white'},
                                    baxis: {gridcolor: isDarkMode ? '#506784': 'white', 
                                            linecolor: isDarkMode ? '#506784': 'white'},
                                    bgcolor: isDarkMode ? 'rgb(17,17,17)': '#E5ECF6',
                                    caxis: {gridcolor: isDarkMode ? '#506784': 'white', 
                                            linecolor: isDarkMode ? '#506784': 'white'}
                                    },
                            font: {color: isDarkMode ? '#f2f5fa': 'rgb(36,36,36)'
                                },
                            };

        document.querySelectorAll('.plotly-graph-div').forEach(function (plotDiv) {
            const currentLayout = plotDiv.layout || {}; // Retrieve current layout if available            
            // Preserve unique titles for each plot
            const plotSpecificLayout = {
                    ...plotLayout, // Apply shared layout changes
                    xaxis: {
                        ...plotLayout.xaxis,
                        title: {
                            ...plotLayout.xaxis.title,
                            text: currentLayout.xaxis?.title?.text || '' // Preserve current x-axis title
                        }
                    },
                    yaxis: {
                        ...plotLayout.yaxis,
                        title: {
                            ...plotLayout.yaxis.title,
                            text: currentLayout.yaxis?.title?.text || '' // Preserve current y-axis title
                        }
                    }
                };
        
                Plotly.relayout(plotDiv, plotSpecificLayout);
            });
    }

    // Loop through each dropdown menu
    themeDropdowns.forEach(dropdownMenu => {
        // Select buttons with data-bs-theme-value inside each dropdown
        const themeButtons = dropdownMenu.querySelectorAll('[data-bs-theme-value]');
        
        dropdownMenu.addEventListener('click', (event) => {
            const targetButton = event.target.closest('[data-bs-theme-value]');
            if (targetButton) {
                // Get the theme value
                const themeValue = targetButton.getAttribute('data-bs-theme-value');
                // Update the Plotly background based on selected theme
                updatePlotBackground(themeValue);
            }
        });
    });
});