var ractive = new Ractive({
  target: '#target',
  template: '#template',
  data: {
    // placeholder image data
    image: {
      src: '/img/gifs/problem.gif',
      caption: 'Trying to work out a problem after the 5th hour'
    }
  }
});