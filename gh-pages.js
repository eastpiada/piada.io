import { publish } from 'gh-pages';

publish(
    'build', // path to public directory
    {
        branch: 'gh-pages',
        repo: 'https://github.com/eastpiada/test.piada.io.git',
        user: {
            name: 'Tony',
            email: 'tony.burger@gmail.com'
        },
        dotfiles: true
    },
    () => {
        console.log('Deploy Complete!');
    }
);
