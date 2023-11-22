if ! tmux has-session -t scanner; then
    tmux new -s scanner -d
    tmux send-keys -t scanner:0.0 "bash ./run_app_prod.sh" Enter
fi
    tmux attach -t scanner