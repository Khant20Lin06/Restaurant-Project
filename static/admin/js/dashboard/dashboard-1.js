

(function($) {
    /* "use strict" */
	
 var dlabChartlist = function(){
	var screenWidth = $(window).width();
		//let draw = Chart.controllers.line.__super__.draw; //draw shadow
	var marketChart = function(){
		 var options = {
          series: [{
          name: 'this week',
          data: [1200, 1500, 1100, 1700, 1600, 2000]  // this week (sales in $)
        }, {
          name: 'last week',
          data: [1000, 1300, 900, 1500, 1400, 1800]
        }],
          chart: {
          height: 280,
          type: 'area',
		  toolbar:{
			  show:false
		  }
        },
		colors:["var(--rgba-primary-1)","#f5a792"],
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth',
		  width:3,
		  colors:["var(--primary)","var(--secondary)"],
        },
		legend:{
			show:false
		},
		grid:{
			show:false,
			strokeDashArray: 6,
			borderColor: '#dadada',
		},
		yaxis: {
		  labels: {
			style: {
				colors: '#B5B5C3',
				fontSize: '12px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			},
			formatter: function (value) {
			  return value + "k";
			}
		  },
		},
        xaxis: {
          categories: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"],
		  labels:{
			  style: {
				colors: '#B5B5C3',
				fontSize: '12px',
				fontFamily: 'Poppins',
				fontWeight: 400
				
			},
		  }
        },
		fill:{
			type:'solid',
			opacity:0.05
		},
        tooltip: {
          x: {
            format: 'dd/MM/yy HH:mm'
          },
        },
        };

        var chart = new ApexCharts(document.querySelector("#marketChart"), options);
        chart.render();

		jQuery('#dzOldSeries').on('change',function(){
			jQuery(this).toggleClass('disabled');
			chart.toggleSeries('series1');
		});
		
		jQuery('#dzNewSeries').on('change',function(){
			jQuery(this).toggleClass('disabled');
			chart.toggleSeries('series2');
		});
	}
	var chartTimeline = function(){
		
		var optionsTimeline = {
			chart: {
				type: "bar",
				height: 300,
				stacked: true,
				toolbar: {
					show: false
				},
				sparkline: {
					//enabled: true
				},
				backgroundBarRadius: 5,
				offsetX: -10,
			},
			series: [
				{
					name: "New Customers",
					data: [12, 18, 15, 20, 25, 30, 22]
				},
				{
					name: "Returning Customers",
					data: [-20, -22, -18, -25, -30, -28, -35]
				}
				],
				xaxis: {
				categories: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
				},

			
			plotOptions: {
				bar: {
					columnWidth: "45%",
					endingShape: "rounded",
					colors: {
						backgroundBarColors: ['rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)', 'rgba(0,0,0,0)'],
						backgroundBarOpacity: 1,
						backgroundBarRadius: 5,
						opacity:0
					},

				},
				distributed: true
			},
			colors:['var(--primary)', 'var(--secondary)'],
			
			grid: {
				show: true,
			},
			legend: {
				show: false
			},
			fill: {
				opacity: 1
			},
			dataLabels: {
				enabled: false,
				colors:['#dd2f6e', '#3e4954'],
				dropShadow: {
					enabled: true,
					top: 1,
					left: 1,
					blur: 1,
					opacity: 1
				}
			},
			xaxis: {
				categories: ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
				labels: {
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				},
				crosshairs: {
					show: false,
				},
				axisBorder: {
					show: false,
				},
			},
			
			yaxis: {
				//show: false
				labels: {
					style: {
						colors: '#787878',
						fontSize: '13px',
						fontFamily: 'Poppins',
						fontWeight: 400
						
					},
				},
			},
			
			tooltip: {
				x: {
					show: true
				}
			}
    };
		var chartTimelineRender =  new ApexCharts(document.querySelector("#chartTimeline"), optionsTimeline);
		 chartTimelineRender.render();
	}
	var overiewChart = function(){
		 var options = {
        series: [{
			name: 'Monthly Sales ($)',
			type: 'column',
			data: [8000, 9500, 8700, 11000, 12000, 10500, 9500, 13000, 12500, 11500, 14000, 15000]
			}, {
			name: 'Orders Served',
			type: 'area',
			data: [400, 500, 480, 600, 620, 550, 500, 650, 640, 610, 700, 750]
			}, {
			name: 'Active Dishes',
			type: 'line',
			data: [25, 28, 30, 32, 30, 35, 33, 34, 36, 35, 38, 40]
			}],
          chart: {
          height: 300,
          type: 'line',
          stacked: false,
		  toolbar: {
				show: false,
			},
        },
        stroke: {
          width: [0, 1, 1],
          curve: 'straight',
		  dashArray: [0, 0, 5]
        },
		legend: {
			fontSize: '13px',
			fontFamily: 'poppins',
			 labels: {
				  colors:'#888888', 
			 }
		},
        plotOptions: {
          bar: {
            columnWidth: '18%',
			 borderRadius:6	,
          }
        },
        
        fill: {
          //opacity: [0.1, 0.1, 1],
		  type : 'gradient',
          gradient: {
            inverseColors: false,
            shade: 'light',
            type: "vertical",
            /* opacityFrom: 0.85,
            opacityTo: 0.55, */
			colorStops : [
				[
					{
					  offset: 0,
					  color: 'var(--primary)',
					  opacity: 1
					},
					{
					  offset: 100,
					  color: 'var(--primary)',
					  opacity: 1
					}
				],
				[
					{
					  offset: 0,
					  color: '#3AC977',
					  opacity: 1
					},
					{
					  offset: 0.4,
					  color: '#3AC977',
					  opacity: .15
					},
					{
					  offset: 100,
					  color: '#3AC977',
					  opacity: 0
					}
				],
				[
					{
					  offset: 0,
					  color: '#FF5E5E',
					  opacity: 1
					},
					{
					  offset: 100,
					  color: '#FF5E5E',
					  opacity: 1
					}
				],
			],
            stops: [0, 100, 100, 100]
          }
        },
		colors:["var(--primary)","#3AC977","#FF5E5E"],
         labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ], 
        markers: {
          size: 0
        },
        xaxis: {
          type: 'month',
		  labels: {
			   style: {
				   fontSize: '13px',
				   colors:'#888888',
			   },
		  },
		  
        },
        yaxis: {
          min: 0,
		  tickAmount: 4,
		  labels: {
			   style: {
				   fontSize: '13px',
				   colors:'#888888',
			   },
		  },
        },
        tooltip: {
          shared: true,
          intersect: false,
          y: {
            formatter: function (y) {
              if (typeof y !== "undefined") {
                return y.toFixed(0) + " points";
              }
              return y;
        
            }
          }
        }
        };

        var chart = new ApexCharts(document.querySelector("#overiewChart"), options);
        chart.render();
		
		$(".mix-chart-tab .nav-link").on('click',function(){
			var seriesType = $(this).attr('data-series');
			var columnData = [];
			var areaData = [];
			var lineData = [];
			var newLabels = [];

			switch(seriesType) {
    case "week":
        // Weekly (Sun–Sat)
        columnData = [1200, 1500, 1100, 1700, 1600, 2000, 1800];  // Sales ($)
        areaData   = [90, 110, 95, 130, 125, 160, 150];           // Orders
        lineData   = [25, 26, 28, 29, 30, 32, 33];                // Active Dishes
        newLabels  = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
        break;

    case "month":
        // Monthly (Jan–Dec)
        columnData = [8500, 9500, 8700, 11000, 12000, 10500, 9800, 13000, 12500, 11500, 14000, 15000]; // Sales ($)
        areaData   = [420, 480, 460, 540, 600, 560, 530, 620, 610, 580, 660, 700];                     // Orders
        lineData   = [25, 26, 28, 30, 29, 31, 32, 33, 34, 33, 35, 36];                                // Active Dishes
        newLabels  = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];
        break;

    case "year":
        // Yearly (past years)
        columnData = [95000, 105000, 120000, 135000, 150000, 165000, 172000, 180000, 190000, 205000, 210000, 225000]; // Annual sales
        areaData   = [5200, 5400, 5900, 6200, 6400, 6700, 7000, 7200, 7600, 7800, 8000, 8300];                         // Orders served
        lineData   = [25, 26, 27, 29, 30, 31, 33, 34, 35, 36, 37, 38];                                                 // Avg dishes on menu
        newLabels  = ['2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025', '2026'];
        break;

    case "all":
        // All-time combined
        columnData = [1000, 1500, 1300, 1700, 1900, 1800, 1600, 1750, 1900, 1850, 2000, 2200];
        areaData   = [80, 100, 90, 120, 130, 125, 110, 115, 130, 125, 135, 140];
        lineData   = [25, 27, 28, 30, 32, 31, 30, 31, 33, 34, 35, 36];
        newLabels  = ['Q1', 'Q2', 'Q3', 'Q4', 'Y1', 'Y2', 'Y3', 'Y4', 'Y5', 'Y6', 'Y7', 'Y8'];
        break;

    default:
        columnData = [1200, 1500, 1100, 1700, 1600, 2000, 1800];
        areaData   = [90, 110, 95, 130, 125, 160, 150];
        lineData   = [25, 26, 28, 29, 30, 32, 33];
        newLabels  = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
}

			chart.updateOptions({
			  labels: newLabels
			});
			chart.updateSeries([
				{
					name: "Monthly Sales ($)",
					type: 'column',
					data: columnData
					
					
				},{
					name: 'Orders Served',
					type: 'area',
					data: areaData
					
				},{
					name: 'Active Dishes',
					type: 'line',
					data: lineData
					
				}
			]);
		})
	 
	}
	var NewCustomers = function(){
			var options = {
					  series: [
						{
							name: 'Net Profit',
							data: [70, 150, 100, 200, 100, 150, 150,70],
						}, 				
					],
					chart: {
						type: 'area',
						height: 100,
						width: 400,
						toolbar: {
							show: false,
						},
						zoom: {
							enabled: false
						},
						sparkline: {
							enabled: true
						}
						
					},
			
					colors:['#2696FD'],
					
					dataLabels: {
					  enabled: false,
					},

				legend: {
					show: false,
				},
				stroke: {
				  show: true,
				  width: 3,
				  curve:'smooth',
				  colors:['#4CBC9A'],
				},
			
				 states: {
						normal: {
							filter: {
								type: 'none',
								value: 0
							}
						},
						hover: {
							filter: {
								type: 'none',
								value: 0
							}
						},
						active: {
							allowMultipleDataPointsSelection: false,
							filter: {
								type: 'none',
								value: 0
							}
						}
				},
					xaxis: {
						categories: ['Jan', 'feb', 'Mar', 'Apr', 'May'],
						axisBorder: {
							show: false,
						},
						axisTicks: {
							show: false
						},
						labels: {
							show: false,
							style: {
								fontSize: '12px',
							}
						},
						crosshairs: {
							show: false,
							position: 'front',
							stroke: {
								width: 2,
								dashArray: 3
							}
						},
						tooltip: {
							enabled: true,
							formatter: undefined,
							offsetY: 0,
							style: {
								fontSize: '12px',
							}
						}
					},
				yaxis: {
					show: false,
				},
				fill: {
					type:'solid',
				  opacity: 0.1,
				  colors:'#4CBC9A'
				},
				tooltip: {
					enabled:false,
					style: {
						fontSize: '12px',
					},
					y: {
						formatter: function(val) {
							return "$" + val + " thousands"
						}
					}
				},
				responsive:[
					{
						breakpoint: 1601,
						options:{
							chart: {
								height:80,
							},
							
						},
						breakpoint: 1401,
						options:{
							chart: {
								width:'100%',
							},
							
						}
					}
				]
			};
            var chartBar1 = new ApexCharts(document.querySelector("#NewCustomers"), options);
            chartBar1.render();
        }
		
	var swipercard = function() {
		var swiper = new Swiper('.mySwiper-counter', {
			speed: 1500,	
			slidesPerView: 4,
			spaceBetween: 40,
			parallax: true,
			loop:false,
			breakpoints: {
				
			  300: {
				slidesPerView: 1,
				spaceBetween: 30,
			  },	
			  576: {
				slidesPerView: 2,
				spaceBetween: 30,
			  },
			  991: {
				slidesPerView: 3,
				spaceBetween: 30,
			  },
			  1200: {
				slidesPerView: 4,
				spaceBetween: 30,
			  },
			},
		});
	}
	
	var handleDatetimepicker = function(){
		if(jQuery("#datetimepicker1").length>0) {
			$('#datetimepicker1').datetimepicker({
				inline: true,
			});
		}
	}
	var chartBarRunning = function(){
		var options  = {
			series: [
				{
					name: 'Income',
					data: [51, 98, 75,35, 64, 44,44]
				}, 
				{
				  name: 'Expense',
				   data: [23, 32, 45,75, 35, 66, 84]
				}, 
				
			],
			chart: {
			type: 'bar',
			height: 300,
			
			
			toolbar: {
				show: false,
			},
			
		},
		plotOptions: {
		  bar: {
			horizontal: false,
			endingShape:'rounded',
			columnWidth: '45%',
			borderRadius: 5,
			
		  },
		},
		colors:[ '#FCC43E','#FB7D5B'],
		dataLabels: {
		  enabled: false,
		},
		markers: {
			shape: "circle",
		},
		legend: {
			show: false,
			fontSize: '12px',
			labels: {
				colors: '#000000',
				
				},
			markers: {
			width: 30,
			height: 30,
			strokeWidth: 0,
			strokeColor: '#fff',
			fillColors: undefined,
			radius: 35,	
			}
		},
		stroke: {
			show: true,
			width: 6,
		},
		xaxis: {
			categories: ['Mon', 'Tue', 'Wed','Thu','Fri','Sat','Sun'],
			labels: {
				style: {
					fontSize: '13px',
					fontFamily: 'poppins',
					fontWeight: 100,
					cssClass: 'apexcharts-xaxis-label',
				},
			},
			axisBorder: {
				show: false,
			},
			axisTicks: {
				show: false,
				borderType: 'solid',
				color: '#78909C',
				height: 6,
				offsetX: 0,
				offsetY: 0
			},
			crosshairs: {
				show: false,
			}
		},
		yaxis: {
			labels: {
				offsetX:-16,
				style: {
					fontSize: '13px',
					fontFamily: 'poppins',
					fontWeight: 100,
					cssClass: 'apexcharts-xaxis-label',
				},
			},
		},
		fill: {
		  opacity: 1,
		},
		tooltip: {
		  y: {
			formatter: function (val) {
			  return "$ " + val + " thousands"
			}
		  }
		},
		grid: {
			borderColor: '#C1BBEB',
			xaxis: {
				lines: {
					show: false
				},
			},
			yaxis: {
				lines: {
					show: true
				},
			},  
		},
		responsive: [{
			breakpoint: 575,
			options: {
				plotOptions: {
				  bar: {
					columnWidth: '1%',
					borderRadius: -1,
				  },
				},
				chart:{
					height:250,
				},
				series: [
					{
						name: 'Projects',
						 data: [31, 40, 28,31, 40, 28,31, 40]
					}, 
					{
					  name: 'Projects',
					   data: [11, 32, 45,31, 40, 28,31, 40]
					}, 
					
				],
			}
		 }]
		};

		if(jQuery("#chartBarRunning").length > 0){

			var chart = new ApexCharts(document.querySelector("#chartBarRunning"), options);
			chart.render();
            
            jQuery('#dzOldSeries1').on('change',function(){
                jQuery(this).toggleClass('disabled');
                chart.toggleSeries('Income');
            });
            
            jQuery('#dzNewSeries1').on('change',function(){
                jQuery(this).toggleClass('disabled');
                chart.toggleSeries('Expense');
            });
            
		}
			
	}
	
	
 
	/* Function ============ */
		return {
			init:function(){
		},
			
			
			load:function(){
				handleDatetimepicker();
				chartBarRunning();
				swipercard();
				marketChart();
				//NewCustomers();
				//chartTimeline();
				overiewChart();
			},
			
			resize:function(){
				chartBarRunning();
			}
		}
	}();

	
		
	jQuery(window).on('load',function(){
		setTimeout(function(){
			dlabChartlist.load();
		}, 1000); 
		
	});

     

})(jQuery);