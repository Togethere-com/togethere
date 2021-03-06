var gulp = require('gulp'),
    sass = require('gulp-sass'),
    autoprefixer = require('gulp-autoprefixer'),
    cleancss = require('gulp-clean-css'),
    // jshint = require('gulp-jshint'),
    uglify = require('gulp-uglify'),
    imagemin = require('gulp-imagemin'),
    rename = require('gulp-rename'),
    // concat = require('gulp-concat'),
    notify = require('gulp-notify'),
    cache = require('gulp-cache'),
    livereload = require('gulp-livereload'),
    del = require('del'),
    browserify = require('browserify'),
    source = require('vinyl-source-stream'),
    buffer = require('vinyl-buffer'),
    sourcemaps = require('gulp-sourcemaps'),
    gutil = require('gulp-util'),
    babelify = require('babelify');

gulp.task('styles', function() {
  return gulp.src(['src/styles/main.scss','src/styles/vendor/tinymce.scss'])
  .pipe(sass().on('error', sass.logError))
  .pipe(autoprefixer('last 2 version'))
  .pipe(gulp.dest('build/css'))
  .pipe(rename({suffix: '.min'}))
  .pipe(cleancss())
  .pipe(gulp.dest('build/css'))
  .pipe(notify({ message: 'Styles task complete' }));
});

gulp.task('mainjs', function () {
  var b = browserify({
    entries: ['src/scripts/modernizr.js', 'src/scripts/main.js'],
    debug: true
  }).transform(babelify, { presets: ["latest"] })

  return b.bundle()
    .pipe(source('main.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({loadMaps: true}))
        // Add transformation tasks to the pipeline here.
        // .pipe(uglify())
        .on('error', gutil.log)
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('build/js/'));
});

gulp.task('likejs', function () {
  var b = browserify({
    entries: ['src/scripts/like.js'],
    debug: true
  }).transform(babelify, { presets: ["latest"] })

  return b.bundle()
    .pipe(source('like.js'))
    .pipe(buffer())
    .pipe(sourcemaps.init({loadMaps: true}))
        // Add transformation tasks to the pipeline here.
        // .pipe(uglify())
        .on('error', gutil.log)
    .pipe(sourcemaps.write('./'))
    .pipe(gulp.dest('build/js/'));
});

gulp.task('images', function() {
  return gulp.src('src/images/**/*')
  .pipe(cache(imagemin({ optimizationLevel: 5, progressive: true, interlaced: true })))
  .pipe(gulp.dest('build/img'))
  .pipe(notify({ message: 'Images task complete' }));
});

gulp.task('clean', function() {
  return del(['build/css', 'build/js', 'build/img']);
});

gulp.task('default', ['clean'], function() {
  gulp.start('styles', 'mainjs', 'likejs', 'images');
});

gulp.task('watch', function() {
  // Watch .scss files
  gulp.watch('src/styles/**/*.scss', ['styles']);
  // Watch .js files
  gulp.watch('src/scripts/**/*.js', ['mainjs', 'likejs']);
  // Watch image files
  gulp.watch('src/images/**/*', ['images']);
  // Create LiveReload server
  livereload.listen();
  // Watch any files in dist/, reload on change
  gulp.watch(['build/**']).on('change', livereload.changed);

});
