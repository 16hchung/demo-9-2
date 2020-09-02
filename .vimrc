set number
set autoindent
set listchars+=tab:>>
set listchars+=space:␣
set listchars+=eol:¬
set list
" Nmap oo o<Esc>k
filetype plugin indent on
syntax on

nmap oo o<Esc>k

" Highlight all instances of word under cursor, when idle.
" Useful when studying strange source code.
" Type z/ to toggle highlighting on/off.
nnoremap z/ :if AutoHighlightToggle()<Bar>set hls<Bar>endif<CR>
function! AutoHighlightToggle()
    let @/ = ''
    if exists('#auto_highlight')
        au! auto_highlight
        augroup! auto_highlight
        setl updatetime=4000
        echo 'Highlight current word: off'
        return 0
    else
        augroup auto_highlight
            au! 
            au CursorHold * let @/ = '\V\<'.escape(expand('<cword>'), '\').'\>'
        augroup end 
        setl updatetime=500
        echo 'Highlight current word: ON'
        return 1
    endif
endfunction

" file navigation
let g:netrw_liststyle=3
let g:netrw_banner=0
let g:netrw_browse_split=4
let g:netrw_winsize=15
let g:netrw_altv=1

augroup custom_highlighting
    autocmd!
    autocmd VimEnter,WinEnter * match SpellCap /QUESTION/
augroup END

set colorcolumn=80
