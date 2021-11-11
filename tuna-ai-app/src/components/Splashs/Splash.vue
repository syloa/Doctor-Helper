<template>
    <div>
      <Particles
        id="tsparticles"  
        :options="{
            background: {
                color: {
                    value: '#0d47a1'
                }
            },
            fpsLimit: 60,
            interactivity: {
                detectsOn: 'canvas',
                events: {
                    onClick: {
                        enable: true,
                        mode: 'push'
                    },
                    onHover: {
                        enable: true,
                        mode: 'repulse'
                    },
                    resize: true
                },
                modes: {
                    bubble: {
                        distance: 400,
                        duration: 2,
                        opacity: 0.8,
                        size: 40
                    },
                    push: {
                        quantity: 4
                    },
                    repulse: {
                        distance: 200,
                        duration: 0.4
                    }
                }
            },
            fullScreen: {
              enable: true,
              zIndex: -1
            },
            particles: {
                color: {
                    value: '#ffffff'
                },
                links: {
                    color: '#ffffff',
                    distance: 150,
                    enable: true,
                    opacity: 0.5,
                    width: 1
                },
                collisions: {
                    enable: true
                },
                move: {
                    direction: 'none',
                    enable: true,
                    outMode: 'bounce',
                    random: false,
                    speed: 6,
                    straight: false
                },
                number: {
                    density: {
                        enable: true,
                        value_area: 800
                    },
                    value: 80
                },
                opacity: {
                    value: 0.5
                },
                shape: {
                    type: 'circle'
                },
                size: {
                    random: true,
                    value: 5
                }
            },
            detectRetina: true
        }"
      />
      <div class="q-pa-lg">
          <br>
        <div class="text-h3 text-weight-bolder row justify-center" style="color:white ; "> Doctor Helper </div>
        <div class="text-h6 text-weight-bolder row justify-center" style="color:white ; "> <br>AI Medical Imaging Analysis <br>
 </div>
       </div> <div class="q-pa-lg row justify-center">
        <q-img  style="width: 345px" src="~assets/icons/doctorHelperlogo.png" /> 
      </div>
      </div>
</template>
<script>
export default {
    name: 'Splash',
}
</script>