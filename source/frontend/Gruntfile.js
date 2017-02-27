/*global module:false*/
module.exports = function(grunt) {

  // Project configuration.
  grunt.initConfig({

    // Task configuration.
    // Using the BrowserSync Server for your static .html files.
    browserSync: {
      default_options: {
        bsFiles: {
          src: [
            "static/css/*.css",
            "*.html"
          ]
        },
        options: {
          watchTask: true,
          server: { // Disable when you are using own webserver
            baseDir: "./"
          }
          // proxy: "yourvhost.dev" Enable when you are using own webserver
        }
      }
    },
    uglify: {
      options: {
        banner: '<%= banner %>'
      },
      dist: {
        src: '<%= concat.dist.dest %>',
        dest: 'js/<%= pkg.name %>.min.js'
      }
    },
    sass: {
      dist: {
        files: {
          // destination         // source file
          "static/css/main.css" : "sass/main.scss"
        },
        options: {
          // loadPath: require('node-bourbon').with('other/path', 'another/path')
          // - or -
          style: "compressed",
          loadPath: require('node-bourbon').includePaths
          //loadPath: require('node-neat').includePaths
        },
      }
    },
    watch: {
      sass: {
        files: "sass/*.scss",
        tasks: ['sass']
      },
      js: {
          files: ['js/main.js'],
          tasks: ['uglify']
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-browser-sync');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-watch');

  // Default task.
  grunt.registerTask('default', ['browserSync', 'watch']);

};
