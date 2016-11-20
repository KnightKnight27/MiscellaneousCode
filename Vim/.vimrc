syntax on
filetype on
filetype plugin indent on

set hlsearch
set ignorecase
set pastetoggle=<F10>

" TODO(andy): extend to hs files
set expandtab
set shiftwidth=4
set tabstop=4

autocmd BufNewFile,BufRead *.py,*.pyx set smartindent cinwords=if,elif,else,for,while,try,except,finally,def,class,inline,with
autocmd BufNewFile,BufRead *.py,*.pyx set softtabstop=4
autocmd BufNewFile,BufRead *.py,*.pyx set tabstop=4
autocmd BufNewFile,BufRead *.py,*.pyx set shiftwidth=4
autocmd BufNewFile,BufRead *.py,*.pyx set textwidth=79
autocmd BufNewFile,BufRead *.py,*.pyx set expandtab
autocmd BufNewFile,BufRead *.py,*.pyx set autoindent
autocmd BufNewFile,BufRead *.py,*.pyx set smarttab
autocmd BufNewFile,BufRead *.py,*.pyx set fileformat=unix
autocmd BufNewFile,BufRead *.py,*.pyx highlight BadTrailingWhitespace ctermbg=red guibg=red
autocmd BufNewFile,BufRead *.py,*.pyx highlight BadLeadingWhitespace ctermbg=red guibg=red
autocmd BufNewFile,BufRead *.py,*.pyx highlight OverLength ctermbg=red guibg=red
autocmd BufNewFile,BufRead *.py,*.pyx match OverLength /\%79v.*/
autocmd BufNewFile,BufRead *.py,*.pyx match BadLeadingWhitespace /^\t\+/
autocmd BufNewFile,BufRead *.py,*.pyx match BadTrailingWhitespace /\s\+$/

autocmd BufNewFile,BufRead *.pl set tabstop=4
autocmd BufNewFile,BufRead *.pl set shiftwidth=4
autocmd BufNewFile,BufRead *.pl set smarttab
autocmd BufNewFile,BufRead *.pl set expandtab
autocmd BufNewFile,BufRead *.pl set softtabstop=4
autocmd BufNewFile,BufRead *.pl set autoindent

autocmd BufNewFile,BufRead *.sh set tabstop=4
autocmd BufNewFile,BufRead *.sh set shiftwidth=4
autocmd BufNewFile,BufRead *.sh set smarttab
autocmd BufNewFile,BufRead *.sh set expandtab
autocmd BufNewFile,BufRead *.sh set softtabstop=4
autocmd BufNewFile,BufRead *.sh set autoindent

autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set tabstop=4
autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set shiftwidth=4
autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set smarttab
autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set expandtab
autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set softtabstop=4
autocmd BufNewFile,BufRead *.cpp,*.h,*.c,*.hpp set autoindent

autocmd BufNewFile,BufRead *.lisp set tabstop=4
autocmd BufNewFile,BufRead *.lisp set shiftwidth=4
autocmd BufNewFile,BufRead *.lisp set smarttab
autocmd BufNewFile,BufRead *.lisp set expandtab
autocmd BufNewFile,BufRead *.lisp set softtabstop=4
autocmd BufNewFile,BufRead *.lisp set autoindent

autocmd BufNewFile,BufRead *.sql set filetype=mysql

map <BS> <PageUp>
map <Space> <PageDown>
